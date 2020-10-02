from django.test import TestCase

# Create your tests here.

def test_case(self):
	if self and self.note:
		print("Note already exists")
		return
	# If no notes found it should return sample note
	note = "This is sample note for test case"
	return note
