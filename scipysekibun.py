from scipy import integrate

def func(x):
      return  2*x+5
result, err = integrate.quad(func,0,5)
print('積分結果:{0}\n誤差:{1}'.format(result,err))
