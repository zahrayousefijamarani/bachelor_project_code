w1 = [
 [-1,  1,  1,  1, -1, -1],
 [-1,  1,  1,  1, -1,  1],
 [ 1, -1, -1, -1, -1,  1],
 [-1, -1,  1, -1, -1, -1],
 [-1,  1, -1,  1,  1, -1],
 [ 1, -1, -1,  1,  1,  1],
 [-1, -1,  1, -1, -1, -1],
 [-1,  1, -1,  1, -1,  1],
 [ 1, -1,  1,  1,  1,  1],
 [ 1,  1, -1, -1, -1, -1],
 [-1, -1,  1, -1, -1,  1],
 [-1,  1, -1,  1,  1, -1]]

w2 = [[-1,  1, -1, -1,  1, -1, -1, -1,  1, -1,  1,  1]]


def generate_code(row, column):
  print("* Memory Simulation\n")
  for i in range(0, row):
    for j in range(0, column):
      print(f"******** cell{i}{j} *********") # for xj
      if w1[i][j] == 1:
        print(f"XMTJ{i}{j}_0 NetBL{j}_0 Net{i}{j}_0 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='0' Kp='1.08e7'")
        print(f"MQ{i}{j}_0 Net{i}{j}_0 NetWL{i} NetSL{i} NetSL{i} MCH3484 l=45nm w=400um")

        print(f"XMTJ{i}{j}_1 NetBL{j}_1 Net{i}{j}_1 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
        print(f"MQ{i}{j}_1 Net{i}{j}_1 NetWL{i} NetSL{i} NetSL{i} MCH3484 l=45nm w=400um")
      elif w1[i][j] == -1: 
        print(f"XMTJ{i}{j}_0 NetBL{j}_0 Net{i}{j}_0 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
        print(f"MQ{i}{j}_0 Net{i}{j}_0 NetWL{i} NetSL{i} NetSL{i} MCH3484 l=45nm w=400um")

        print(f"XMTJ{i}{j}_1 NetBL{j}_1 Net{i}{j}_1 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='0' Kp='1.08e7'")
        print(f"MQ{i}{j}_1 Net{i}{j}_1 NetWL{i} NetSL{i} NetSL{i} MCH3484 l=45nm w=400um")

      print("**************************\n")

  print("\n********** Word Line *********")
  for i in range(0, row):
    #print(f"V{i} NetWL{i} 0 PULSE (0V 0.7V {i*5+5}us 0us 0us 4.5us {row*5+5}us)") 
    print(f"V{i} NetWL{i} 0 PULSE (0V 0.7V 5us 0us 0us 4.5us 20us)") 
  print("**************************\n")

  print("\n********** Bit Line *********")
  for j in range(0, column):
    print(f"V{j+row}_0 NetBL{j}_0 0 0.3V")#PULSE (0V 0.3V 5us 0.5us 0.5us {row*5+5}us {row*5+10}us) ")  
    print(f"V{j+row}_1 NetBL{j}_1 0 0")#PULSE (0.3V 0V 5us 0.5us 0.5us {row*5+5}us {row*5+10}us) ")
    print()
  print("**************************\n")


  print("\n********** OpAMP *********")
  for i in range(0, row):
    print(f"E_opamp{i} Net_opamp{i} 0 VCVS NetSL{i} Net_op{i} 1E6 max=0.3 min=0")   
    print(f"V{i}_ref Net_op{i} 0 160mv")
    print()
  print("**************************\n")




def generate_code_2(row, column):
  print("* Memory Simulation\n")
  for i in range(0, row):
    for j in range(0, column):
      print(f"******** cell{i}{j} *********") # for xj
      if w2[i][j] == 1:
        print(f"XMTJ{i}{j}_0_1 NetBL{j}_0_1 Net{i}{j}_0_1 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='0' Kp='1.08e7'")
        print(f"MQ{i}{j}_0_1 Net{i}{j}_0_1 NetWL{i}_1 NetSL{i}_1 NetSL{i}_1 MCH3484 l=45nm w=400um")

        print(f"XMTJ{i}{j}_1_1 NetBL{j}_1_1 Net{i}{j}_1_1 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
        print(f"MQ{i}{j}_1_1 Net{i}{j}_1_1 NetWL{i}_1 NetSL{i}_1 NetSL{i}_1 MCH3484 l=45nm w=400um")
      elif w2[i][j] == -1: 
        print(f"XMTJ{i}{j}_0_1 NetBL{j}_0_1 Net{i}{j}_0_1 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
        print(f"MQ{i}{j}_0_1 Net{i}{j}_0_1 NetWL{i}_1 NetSL{i}_1 NetSL{i}_1 MCH3484 l=45nm w=400um")

        print(f"XMTJ{i}{j}_1_1 NetBL{j}_1_1 Net{i}{j}_1_1 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='0' Kp='1.08e7'")
        print(f"MQ{i}{j}_1_1 Net{i}{j}_1_1 NetWL{i}_1 NetSL{i}_1 NetSL{i}_1 MCH3484 l=45nm w=400um")

      print("**************************\n")

  print("\n********** Word Line *********")
  for i in range(0, row):
    #print(f"V{i}_1_2 NetWL{i}_1 0 PULSE (0V 0.7V {i*5+5}us 0us 0us 4.5us {row*5+5}us)") 
    print(f"V{i}_1_2 NetWL{i}_1 0 PULSE (0V 0.7V 5us 0us 0us 4.5us 20us)") 
  print("**************************\n")

  print("\n********** Bit Line *********")
  for j in range(0, column):
    #print(f"V{j+row}_0_1 NetBL{j}_0_1 0 PULSE (0V 0.3V 5us 1ns 1ns {row*5+5}us {row*5+10}us) ")   
    #print(f"V{j+row}_1_1 NetBL{j}_1_1 0 PULSE (0.3V 0V 5us 1ns 1ns {row*5+5}us {row*5+10}us) ")
    print(f"R{j}_0_1 Net_opamp{j} NetBL{j}_0_1 0.01")  
    print(f"MQ{j}_op0 NetBL{j}_1_1 Net_opamp{j} Net_vdd Net_vdd MCH3383 l=45nm w=400um")   
    print(f"MQ{j}_op1 NetBL{j}_1_1 Net_opamp{j} 0 0 MCH3484 l=45nm w=400um")
  
    print()
  print("**************************\n")

  print("\n********** OpAMP *********")
  for i in range(0, row):
    print(f"E_opamp{i}_1 Net_opamp{i}_1 0 VCVS NetSL{i}_1 Net_op{i}_1 1E6 max=0.7 min=0")  
    print(f"V{i}_ref_1 Net_op{i}_1 0 160mv") 
    print()
  print("**************************\n")



generate_code(12, 6)
generate_code_2(1, 12)