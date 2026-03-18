doc = input("Please, enter a document: ")
if doc.endswith(".pdf"):
    print(f"Type of document: {doc}")
elif doc.endswith(".txt"):
     print(f"Type of document: {doc}")
elif doc.endswith(".docx"):
    print(f"Type of document: {doc}")
else:
    print("error type of document!")