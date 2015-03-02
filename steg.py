import os
import threading
import steganography

class Steg:
	def __init__(self, hidden_file_name, cover_file_name):
		try:
			self.chunk_size = 6
			self.hidden_file = open(hidden_file_name, 'r')
			self.cover_file = open(cover_file_name, 'r')
			self.threads = []
		except IOError:
			raise
	def split_hidden_content(self):
		length = os.path.getsize(self.hidden_file.name) - 1
		self.split_indices = [x for x in range(0, length, self.chunk_size)]
	def steganograph(self, output_file_name):
		for i in self.split_indices:
			self.spawn_thread(i, output_file_name)
		for thread_ in self.threads:
			thread_.join()
	def spawn_thread(self, i, output_file_name):
		thread_i = threading.Thread(target=self.encrypt, args=(i, output_file_name))
		self.threads.append(thread_i)
		thread_i.start()
	def encrypt(self, i ,output_file_name):
		output_file = open('outputs' + os.path.sep + output_file_name + str(i) + '.txt', 'w+')
		cover_file = open(self.cover_file.name, 'r')
		hidden_file = open(self.hidden_file.name, 'r')
		hidden_file.seek(i, 0)
		hidden_text = hidden_file.read(self.chunk_size)
		cover_text = cover_file.read()
		output_file.write(steganography.encode(cover_text, hidden_text))
		output_file.close()
		cover_file.close()
		hidden_file.close()

if __name__ == '__main__':
	steganography.init_steganography()
	s = Steg('hidden.txt', 'cover.txt')
	s.split_hidden_content()
	s.steganograph('output')

