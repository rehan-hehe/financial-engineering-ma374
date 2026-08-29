import numpy as np
import matplotlib.pyplot as plt
S_0=9
K=10
T=3
r=0.06
sigma=0.3
def option_val(Ms,part):
    #partc
    counts=[0,0.3,0.75,1.5,2.7]
    all_val = []
    M20_calls={}
    M20_puts={}
    for M in Ms:
        difft=T/M
        rate=np.exp(r*difft)
        discount=np.exp(-r*difft)
        u=np.exp((sigma*np.sqrt(difft))+((r-(0.5*sigma*sigma))*difft))
        d=np.exp(-(sigma*np.sqrt(difft))+((r-(0.5*sigma*sigma))*difft))
        p=(rate-d)/(u-d)
        # checking for no arbitrage: d<rate<u
        if (d<rate and rate<u):
            print("No Arbitrage confirmed")
            #using list of lists to save all steps
            lol=[]
            lol.append([S_0])
            for i in range(1,M+1):
                curr_list=[]
                prev_list=lol[i-1]
                for j in range(len(prev_list)):
                    curr_list.append(prev_list[j]*u)
                    if (j==len(prev_list)-1):
                        curr_list.append(prev_list[j]*d)
                lol.append(curr_list)
            #part a
            #start from Mth step and find option value at prev step
            final_prices=lol[-1]
            call_option_val_at_M=[]
            put_option_val_at_M=[]
            count=3
            for i in range(len(final_prices)):
                call_option_val_at_M.append(max(final_prices[i]-K,0))
                put_option_val_at_M.append(max(K-final_prices[i],0))
            curr_val_call=call_option_val_at_M
            new_val_call=[]
            curr_val_put=put_option_val_at_M
            new_val_put=[]
            for j in range(M):
                count-=0.15
                for i in range(len(curr_val_call)-1):
                    new_val_call.append(discount*((p*curr_val_call[i])+(1-p)*curr_val_call[i+1]))
                curr_val_call=new_val_call
                for target in counts:
                    if M==20 and np.isclose(count,target):
                        M20_calls[target]=new_val_call
                new_val_call=[]
                for i in range(len(curr_val_put)-1):
                    new_val_put.append(discount*((p*curr_val_put[i])+(1-p)*curr_val_put[i+1]))
                curr_val_put=new_val_put
                for target in counts:
                    if M==20 and np.isclose(count,target):
                        M20_puts[target]=new_val_put
                new_val_put=[]
            both_val=[curr_val_call,curr_val_put]
            all_val.append(both_val)
            if part=='a':
                print("call option value for ",M," steps:", curr_val_call)
                print("put option value for",M," steps:", curr_val_put)
            
        else:
            print("Arbitrage found")
    M20={"Calls":M20_calls,"Puts": M20_puts}
    if part=='c':
        return M20
    return all_val

#part a
Ms=[1,5,10,20,50,100,200]
option_val(Ms,'a')

#part b
Ms1=list(range(1,201)) 
Ms2=list(range(5,201,5)) 
results_1 = option_val(Ms1,'b')
results_5 = option_val(Ms2,'b')

calls_1 = [x[0] for x in results_1]
puts_1  = [x[1] for x in results_1]

calls_5 = [x[0] for x in results_5]
puts_5  = [x[1] for x in results_5]

# Plotting
plt.figure(figsize=(12,6))

# Subplot 1: Call Options
plt.subplot(1,2,1)
plt.plot(Ms1,calls_1,label='Step of 1',color='blue',alpha=0.6)
plt.plot(Ms2,calls_5,label='Step of 5',color='red',linestyle='--')
plt.title('Call Option Price Convergence')
plt.xlabel('Number of Steps (M)')
plt.ylabel('Price at t=0')
plt.legend()
plt.grid(True)

# Subplot 2: Put Options
plt.subplot(1,2,2)
plt.plot(Ms1,puts_1,label='Step of 1',color='green',alpha=0.6)
plt.plot(Ms2,puts_5,label='Step of 5',color='orange',linestyle='--')
plt.title('Put Option Price Convergence')
plt.xlabel('Number of Steps (M)')
plt.ylabel('Price at t=0')
plt.legend()
plt.grid(True)

plt.show()

#part c
Msc=[20]
M20=option_val(Msc,'c')
print(M20)