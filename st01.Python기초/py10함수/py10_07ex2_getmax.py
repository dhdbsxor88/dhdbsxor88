# ����� �Լ� �����
# �� ���� ������ �־����� �μ� �߿��� �� ū ���� ã�Ƽ� �̰��� ��ȯ�ϴ� �Լ��� ������.


def getmax(x, y)
  result = None
   if x > y:
        result = x
    else:
        result = y
    return result


def myinput(mesg) : 
    n1 = input(mesg)
    n1 = int(n1)
    return n1

def main() : 
    n1 = myinput("ù° ����")
    n2 = myinput("��° ����")

    val = getmax(n1, n2)
    print(val)

