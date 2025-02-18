# # Import the sleep function from the time module, so
# # that the sleep function can be used in this program.
# from time import sleep

# # Prompt the user to enter her name.
# name = input("Hello! What is your name? ")

# # Print the numbers 3, 2, 1.
# for i in range(3, 0, -1):
#     print(i, flush=True)
#     sleep(0.5)  # Pause for 1/2 second

# # Use a Python f-string to format a greeting
# # for the user and then print the greeting.
# print(f"Welcome to CSE 111, {name}!")

from graphviz import Digraph

# Create a class diagram for the Comment class
diagram = Digraph(format="png")
diagram.attr(rankdir="TB")

# Define the Comment class box
diagram.node("Comment", """\
<<table border="0" cellborder="1" cellspacing="0">
  <tr><td colspan="1" bgcolor="lightblue"><b>Comment</b></td></tr>
  <tr><td align="left">- _name: string</td></tr>
  <tr><td align="left">- _comment: string</td></tr>
  <tr><td align="left">- _timeStamp: DateTime</td></tr>
  <tr><td align="left">+ Comment(name: string, comment: string)</td></tr>
  <tr><td align="left">+ GetUserName(): string</td></tr>
  <tr><td align="left">+ GetUserNComment(): string</td></tr>
  <tr><td align="left">+ GetCommentTextString(): string</td></tr>
</table>>""", shape="none")

diagram.render("Comment_Class_Diagram", format="png", cleanup=True)

"Comment_Class_Diagram.png"



# Correct the label syntax issue and regenerate the diagram

# Redefine the Video class box
diagram.node("Video", """\
<<table border="0" cellborder="1" cellspacing="0">
  <tr><td colspan="1" bgcolor="lightblue"><b>Video</b></td></tr>
  <tr><td align="left">- _title: string</td></tr>
  <tr><td align="left">- _author: string</td></tr>
  <tr><td align="left">- _length: int</td></tr>
  <tr><td align="left">- _comments: List<Comment></td></tr>
  <tr><td align="left">+ Video(title: string, author: string, length: int)</td></tr>
  <tr><td align="left">+ GetCommnetsNumber(): int</td></tr>
  <tr><td align="left">+ GetVideoInfo(): string</td></tr>
  <tr><td align="left">+ AddComment(comment: Comment): void</td></tr>
  <tr><td align="left">+ GetComments(): List<string></td></tr>
</table>>""".replace("<", "&lt;").replace(">", "&gt;"), shape="none")

# Redefine the association between Video and Comment
diagram.edge("Video", "Comment", label="1..*")

diagram.render("Video_Class_Diagram", format="png", cleanup=True)

"Video_Class_Diagram.png"
