w1 = [[-2,  -2,  0,  0,  0,  1,  6,  1,  0,  0],
 [-1,  7,  0,  0,  0, -1, -1, -1, -1, -1],
 [ 6, -1, -1, -1, -1,  3, -5, -3,  0,  0],
 [-4, -3,  0, -1, -1,  4,  2,  2,  0,  0]] 
w2 = [[4 , 5,  4, 3]]

p0 = [1.15 , 1.07 , 0.987 , 0.91 , 0.83 , 0.75 , 0.66 , 0.56]

def generate_code_layer_1(row, column):
  print("* Memory Simulation\n")
  for i in range(0, row):
    for j in range(0, column):
      print(f"******** cell{i}{j} *********") # for xj
      if w1[i][j] < 0:
        print(f"XMTJ{i}{j}_0 NetBL{j}_0 NetSL{i} MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[0]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
        print(f"XMTJ{i}{j}_1 NetBL{j}_1 NetSL{i} MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[-w1[i][j]]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
      elif w1[i][j] > 0:
        print(f"XMTJ{i}{j}_0 NetBL{j}_0 NetSL{i} MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[w1[i][j]]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
        print(f"XMTJ{i}{j}_1 NetBL{j}_1 NetSL{i} MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[0]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
      elif w1[i][j] == 0:
        print(f"XMTJ{i}{j}_0 NetBL{j}_0 NetSL{i} MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[0]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
        print(f"XMTJ{i}{j}_1 NetBL{j}_1 NetSL{i} MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[0]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")

      print("**************************\n")

  print("\n********** Sense Line *********")
  for i in range(0, row):
    #print(f"VIPROBE{i}_0 NetSL{i} 0 DC 0")
    print(f"H_opamp{i} Net_opamp{i} 0 CCVS V_ref{i} 1E6 max=0.3 min=0")
    print(f"V_ref{i} NetSL{i} 0 0")
  print("**************************\n")

  print("\n********** Bit Line *********")
  for j in range(0, column):
    print(f"V{j+row}_0 NetBL{j}_0 0 PULSE (0V 0.3V 5us 0.5us 0.5us 4.5us 10us) ")  
    print(f"V{j+row}_1 NetBL{j}_1 0 PULSE (0V -0.3V 5us 0.5us 0.5us 4.5us 10us) ")  
    print()
  print("**************************\n")

def generate_code_layer_2(row, column):
    print("* Memory Simulation\n")
    for i in range(0, row):
      for j in range(0, column):
        print(f"******** cell{i}{j}_2 *********") # for xj
        if w2[i][j] < 0:
          print(f"XMTJ{i}{j}_0_2 NetBL{j}_0_2 NetSL{i}_2 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[0]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
          print(f"XMTJ{i}{j}_1_2 NetBL{j}_1_2 NetSL{i}_2 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[-w2[i][j]]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
        elif w2[i][j] > 0:
          print(f"XMTJ{i}{j}_0_2 NetBL{j}_0_2 NetSL{i}_2 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[w2[i][j]]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
          print(f"XMTJ{i}{j}_1_2 NetBL{j}_1_2 NetSL{i}_2 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[0]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
        elif w2[i][j] == 0:
          print(f"XMTJ{i}{j}_0_2 NetBL{j}_0_2 NetSL{i}_2 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[0]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")
          print(f"XMTJ{i}{j}_1_2 NetBL{j}_1_2 NetSL{i}_2 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='{p0[0]}' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'")

        print("**************************\n")

    print("\n********** Sense Line *********")
    for i in range(0, row):
      #print(f"VIPROBE{i}_0_2 NetSL_a{i}_2 0 DC 0")
      #print(f"MQ_SL{i} NetSL{i}_2 Net_gate{i} NetSL_a{i}_2 NetSL_a{i}_2 MCH3484 l=45nm w=400um")
      #print(f"V_sl{i} Net_gate{i} 0 1V")
      print(f"H_opamp_sl{i} Net_opamp_sl{i} CCVS V_ref_sl{i} 1E6 max=0.3 min=0")
      print(f"V_ref_sl{i} NetSL{i}_2 0 0")
      #print(f"VIPROBE{i}_1 NetSL{i}_1 0 DC 0") 
    print("**************************\n")

    print("\n********** Bit Line *********")
    for j in range(0, column):
      #print(f"V{j+row}_0_2 NetBL{j}_0_2 0 PULSE (0V 0.3V 5us 0.5us 0.5us 4.5us 10us) ")  
      #print(f"V{j+row}_1_2 NetBL{j}_1_2 0 PULSE (0V -0.3V 5us 0.5us 0.5us 4.5us 10us) ") 
      print(f"R_SL{j} Net_opamp{j} NetBL{j}_0_2 0.01") 
      print(f"MQ0_op{j}_0 NetBL{j}_1_2 Net_opamp{j} Net_vdd Net_vdd MCH3383 l=45nm w=400um")
      print(f"MQ0_op{j}_1 NetBL{j}_1_2 Net_opamp{j} Net_g Net_g MCH3484 l=45nm w=400um")
      print()
    print("**************************\n")


generate_code_layer_1(4, 10)
generate_code_layer_2(1, 4)