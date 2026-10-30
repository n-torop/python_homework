#Task 1
import traceback

try:
    user_submit=input("What happened today? ")
    with open("diary.txt", "a") as file:
        file.write(user_submit+"\n")
        while True:
        # Type "Done for now" if you want to exit.\n
            continued_input=input('What else? ')
            if continued_input.lower()=="done for now":
                file.write(continued_input+"n")
                break
            file.write(continued_input+"\n")

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")



