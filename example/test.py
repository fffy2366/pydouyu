global msg
msg = ""
def message(m):
	global msg

	if(msg!=m):
		msg = m
		print msg

message("a")
message("a")
message("b")
message("b")