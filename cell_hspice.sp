* Memory Simulation

.include 'MTJ_model.inc'

******** cell00 *********
XMTJ00_0 NetBL0_0 Net00_0 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='0' Kp='1.08e7'
MQ00_0 Net00_0 NetWL0 NetSL0 NetSL0 MCH3484 l=45nm w=400um
XMTJ00_1 NetBL0_1 Net00_1 MTJ lx='40n' ly='116n' lz='1.5n' tox='1.15n' Ms0='850' P0='0.62' alpha='0.028' Tmp0='358' RA0='5' MA='1' ini='1' Kp='1.08e7'
MQ00_1 Net00_1 NetWL0 NetSL0 NetSL0 MCH3484 l=45nm w=400um
**************************

********** Word Line *********
V0 NetWL0 0 PULSE (0V 0.7V 5us 0.5us 0.5us 4.5us 10us)
**************************


********** Bit Line *********
V2_0 NetBL0_0 0 PULSE (0V 0.3V 5us 0.5us 0.5us 4.5us 10us)
V2_1 NetBL0_1 0 PULSE (0.3V 0V 5us 0.5us 0.5us 4.5us 10us)
**************************


************ SIMULATION *********
.tran 10ns 20us
*********************************


.model MCH3484 nmos level = 54 

+version = 4.0             binunit = 1               paramchk= 1               mobmod  = 0             
+capmod  = 2               igcmod  = 1               igbmod  = 1               geomod  = 1             
+diomod  = 1               rdsmod  = 0               rbodymod= 1               rgatemod= 1             
+permod  = 1               acnqsmod= 0               trnqsmod= 0             

+tnom    = 27              toxe    = 9e-010          toxp    = 6.5e-010        toxm    = 9e-010        
+dtox    = 2.5e-010        epsrox  = 3.9             wint    = 5e-009          lint    = 2.7e-009      
+ll      = 0               wl      = 0               lln     = 1               wln     = 1             
+lw      = 0               ww      = 0               lwn     = 1               wwn     = 1             
+lwl     = 0               wwl     = 0               xpart   = 0               toxref  = 9e-010           xl      = -20e-9
+dlcig   = 2.7e-009      

+vth0    = 0.3424         k1      = 0.2             k2      = 0               k3      = 0             
+k3b     = 0               w0      = 2.5e-006        dvt0    = 1               dvt1    = 2             
+dvt2    = 0               dvt0w   = 0               dvt1w   = 0               dvt2w   = 0             
+dsub    = 0.078           minv    = 0.05            voffl   = 0               dvtp0   = 1e-010        
+dvtp1   = 0.1             lpe0    = 0               lpeb    = 0               xj      = 1.4e-008      
+ngate   = 1e+023          ndep    = 6.5e+018        nsd     = 2e+020          phin    = 0             
+cdsc    = 0               cdscb   = 0               cdscd   = 0               cit     = 0             
+voff    = -0.13           nfactor = 1.9             eta0    = 0.0055          etab    = 0             
+vfb     = -1.058          u0      = 0.02947         ua      = -5e-010         ub      = 1.7e-018      
+uc      = 0               vsat    = 159550          a0      = 1               ags     = 0             
+a1      = 0               a2      = 1               b0      = 0               b1      = 0             
+keta    = 0.04            dwg     = 0               dwb     = 0               pclm    = 0.06          
+pdiblc1 = 0.001           pdiblc2 = 0.001           pdiblcb = -0.005          drout   = 0.5           
+pvag    = 1e-020          delta   = 0.01            pscbe1  = 2.0e+009        pscbe2  = 1e-007        
+fprout  = 0.2             pdits   = 0.01            pditsd  = 0.23            pditsl  = 2300000       
+rsh     = 5               rdsw    = 105             rsw     = 52.5            rdw     = 52.5            
+rdswmin = 0               rdwmin  = 0               rswmin  = 0               prwg    = 0             
+prwb    = 0               wr      = 1               alpha0  = 0.074           alpha1  = 0.005         
+beta0   = 30              agidl   = 0.0002          bgidl   = 2.1e+009        cgidl   = 0.0002        
+egidl   = 0.8             aigbacc = 0.012           bigbacc = 0.0028          cigbacc = 0.002         
+nigbacc = 1               aigbinv = 0.014           bigbinv = 0.004           cigbinv = 0.004         
+eigbinv = 1.1             nigbinv = 3               aigc    = 0.018029        bigc    = 0.0029        
+cigc    = 0.002           aigsd   = 0.018029        bigsd   = 0.0029          cigsd   = 0.002         
+nigc    = 1               poxedge = 1               pigcd   = 1               ntox    = 1             
+xrcrg1  = 12              xrcrg2  = 5             

+cgso    = 1e-010          cgdo    = 1e-010          cgbo    = 0               cgdl    = 7.5e-013      
+cgsl    = 7.5e-013        clc     = 1e-007          cle     = 0.6             cf      = 1.1e-010      
+ckappas = 0.6             ckappad = 0.6             vfbcv   = -1              acde    = 1             
+moin    = 15              noff    = 1               voffcv  = 0             

+kt1     = -0.154          kt1l    = 0               kt2     = 0.022           ute     = -1.1          
+ua1     = 1e-009          ub1     = -1e-018         uc1     = -5.6e-011       prt     = 0             
+at      = 33000         

+fnoimod = 1               tnoimod = 0               noia    = 6.25e+041       noib    = 3.125e+026    
+noic    = 8.75e+009       em      = 41000000        af      = 1               ef      = 1             
+kf      = 0               tnoia   = 1.5             tnoib   = 3.5             ntnoi   = 1             

+jss     = 1.2e-006        jsws    = 2.4e-013        jswgs   = 2.4e-013        njs     = 1             
+ijthsfwd= 0.1             ijthsrev= 0.1             bvs     = 10              xjbvs   = 1             
+jsd     = 1.2e-006        jswd    = 2.4e-013        jswgd   = 2.4e-013        xjbvd   = 1             
+pbs     = 1               cjs     = 0.0018          mjs     = 0.5             pbsws   = 1             
+cjsws   = 1.2e-010        mjsws   = 0.33            cjswgs  = 2.1e-010        cjd     = 0.0018        
+cjswd   = 1.2e-010        mjswd   = 0.33            pbswgd  = 1               cjswgd  = 2.1e-010      
+mjswgd  = 0.33            tpb     = 0               tcj     = 0               tpbsw   = 0             
+tcjsw   = 0               tpbswg  = 0               tcjswg  = 0               xtis    = 3             

+dmcg    = 0               dmci    = 0               dmdg    = 0               dmcgt   = 0             
+dwj     = 0               xgw     = 0               xgl     = 0             

+rshg    = 0.4             gbmin   = 1e-010          rbpb    = 5               rbpd    = 15            
+rbps    = 15              rbdb    = 15              rbsb    = 15              ngcon   = 1    


.end