# Tapşırıq 10
class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None

def add_student(head, student_id, student_name, gpa):
    node = StudentNode(student_id, student_name, gpa)
    if head is None:
        return node
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = node
    return head

def delete_student(head, student_id):
    if head and head.student_id == student_id:
        return head.next
    cur = head
    while cur and cur.next:
        if cur.next.student_id == student_id:
            cur.next = cur.next.next
            return head
        cur = cur.next
    print("Bele telebe yoxdur.")
    return head

def show_all(head):
    cur = head
    while cur:
        print(cur.student_id, cur.student_name, cur.gpa, sep="\t")
        cur = cur.next

def show_above_80(head):
    cur = head
    while cur:
        if cur.gpa > 80:
            print(cur.student_id, cur.student_name, cur.gpa, sep="\t")
        cur = cur.next

def search_by_name(head, name):
    cur = head
    while cur:
        if cur.student_name.lower() == name.lower():
            print("Tapildi:", cur.student_id, cur.student_name, cur.gpa)
            return
        cur = cur.next
    print("Tapilmadi.")

def count_students(head):
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next
    return n

head = None
while True:
    print("\n1.Elave 2.Sil 3.Hamisi 4.GPA>80 5.Axtarish 6.Say 0.Cix")
    c = input("Secim: ")
    if c == "1":
        head = add_student(head, input("ID: "), input("Ad: "), float(input("GPA: ")))
    elif c == "2":
        head = delete_student(head, input("ID: "))
    elif c == "3":
        show_all(head)
    elif c == "4":
        show_above_80(head)
    elif c == "5":
        search_by_name(head, input("Ad: "))
    elif c == "6":
        print("Say:", count_students(head))
    elif c == "0":
        break
