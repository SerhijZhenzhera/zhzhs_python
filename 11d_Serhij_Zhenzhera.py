'''
Task 4. Custom exception
Create your custom exception named `CustomException`,
you can inherit from base Exception class,
but extend its functionality to log every error message to a file named `logs.txt`.
Tips: Use __init__ method to extend functionality for saving messages to file
'''

# ----------1---------- [https://all-python.ru/osnovy/obrabotka-isklyuchenij.html]
import logging
logging.basicConfig(filename="logs.txt", level = logging.INFO)
try:
    raise Exception('Custom Exception! \n')
except Exception as e:
    logging.error(str(e))



# ----------2----------
class CustomException(Exception):
    def __init__(self, msg):
        self.message = msg
    
    def raise_e(self):
        try:
            return self.message[10]
        except Exception:
            task_11_4 = open('logs.txt', 'a')
            task_11_4.write('Custom Exception! \n')
            task_11_4.close()
            with open('logs.txt', 'r') as task_11_4:
                print(task_11_4.read())
                return task_11_4.read()
          
if __name__ == "__main__":
    e1 = CustomException('Violetta')
    print(e1.raise_e())
