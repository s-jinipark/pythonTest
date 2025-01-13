
#예외 처리 try except 및 with 문

try:
    val = "10.5"
    n = int(val)
# except:
#     print("오류 발생")

# except ValueError as e:
#     print("오류 발생 {} ".format(e))

except Exception as e:
    print("오류 발생 {} ".format(e))
else: #[셋트]
    print("정상")
finally: 
    print("파이널리 호출")