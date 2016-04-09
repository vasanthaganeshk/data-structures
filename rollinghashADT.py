class rollinghash(object):
	def __init__(self):
		self.val = 0
		self.size = 0
	
	def append(self, char):
		self.val = self.val*256 + ord(char)
		self.size += 1
	
	def pop_left(self, char):
		if self.val == 0:
			raise ValueError("Used pop_left on an empty rollinghash")
		else:
			self.val = self.val - ord(char)*(256**(self.size - 1))
			self.size -= 1

	def hashval(self):
		return self.val%(20988936657440586486151264256610222593863921)