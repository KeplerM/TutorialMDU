
import numpy as np

def ABD(E11,E22,G12,Nu12,Lam,LamTh,PlyN):
#
#
#
#
#
#
 
    i=0
    Th=PlyN*LamTh
    z=[]
    z.append(-Th/2.0)
    
    for j in range (1,PlyN+1,1):
        z.append(z[j-1]+LamTh)

    # Calculate Reduced Stiffness matrix

    Q11=[]
    Q12=[]
    Q16=[]
    Q22=[]
    Q26=[]
    Q66=[]

    Q11_S=[]
    Q12_S=[]
    Q16_S=[]
    Q22_S=[]
    Q26_S=[]
    Q66_S=[]

    for i in range(0,1,1):
        Q11.append((E11/(1-Nu12**2*(E22/E11))))
        Q12.append((Nu12*E11*E22)/(E11-Nu12**2*E22))
        Q16.append(0)
        Q22.append((E11*E22)/(E11-Nu12**2*E22))
        Q26.append(0)
        Q66.append(G12)

    i=0
    for j in range (0,PlyN,1):
        Q11_S.append((Q11[i]*np.cos(Lam[j]*np.pi/180.0)**4)+(Q22[i]*np.sin(Lam[j]*np.pi/180.0)**4)+(2*(Q12[i]+2*Q66[i])*np.cos(Lam[j]*np.pi/180.0)**2*np.sin(Lam[j]*np.pi/180.0)**2))
        Q22_S.append((Q11[i]*np.sin(Lam[j]*np.pi/180.0)**4)+(Q22[i]*np.cos(Lam[j]*np.pi/180.0)**4)+((Q12[i]+2*Q66[i])*np.cos(Lam[j]*np.pi/180)**2*np.sin(Lam[j]*np.pi/180)**2))
        Q12_S.append(((Q11[i]+Q22[i]-4*Q66[i])*np.cos(Lam[j]*np.pi/180.0)**2*np.sin(Lam[j]*np.pi/180.0)**2)+(Q12[i]*(np.cos(Lam[j]*np.pi/180.00)**4+np.sin(Lam[j]*np.pi/180.00)**4)))
        Q66_S.append(((Q11[i]+Q22[i]-2*Q12[i]-2*Q66[i])*np.cos(Lam[j]*np.pi/180)**2*np.sin(Lam[j]*np.pi/180)**2)+(Q66[i]*(np.cos(Lam[j]*np.pi/180.00)**4+np.sin(Lam[j]*np.pi/180.00)**4)))
        Q16_S.append(((Q11[i]-Q12[i]-2*Q66[i])*np.cos(Lam[j]*np.pi/180.00)**3*np.sin(Lam[j]*np.pi/180.00))+((Q12[i]+2*Q66[i]-Q22[i])*np.cos(Lam[j]*np.pi/180.00)*np.sin(Lam[j]*np.pi/180.00)**3))
        Q26_S.append(((Q11[i]-Q12[i]-2*Q66[i])*np.cos(Lam[j]*np.pi/180.00)*np.sin(Lam[j]*np.pi/180.00)**3)+((Q12[i]+2*Q66[i]-Q22[i])*np.cos(Lam[j]*np.pi/180.00)**3*np.sin(Lam[j]*np.pi/180.00)))



    # A matrix


    A11v=[]
    A12v=[]
    A16v=[]
    A22v=[]
    A26v=[]
    A66v=[]
    i=1
    for j in range(0,PlyN,1):
        A11v.append(Q11_S[j]*(z[i]-z[i-1]))
        A12v.append(Q12_S[j]*(z[i]-z[i-1]))
        A16v.append(Q16_S[j]*(z[i]-z[i-1]))
        A22v.append(Q22_S[j]*(z[i]-z[i-1]))
        A26v.append(Q26_S[j]*(z[i]-z[i-1]))
        A66v.append(Q66_S[j]*(z[i]-z[i-1]))
        i=i+1

    A11=sum(A11v)
    A12=sum(A12v)
    A16=sum(A16v)
    A22=sum(A22v)
    A26=sum(A26v)
    A66=sum(A66v)

    # B matrix


    B11v=[]
    B12v=[]
    B16v=[]
    B22v=[]
    B26v=[]
    B66v=[]
    i=1
    for j in range(0,PlyN,1):
        B11v.append(0.5*Q11_S[j]*(z[i]**2-z[i-1]**2))
        B12v.append(0.5*Q12_S[j]*(z[i]**2-z[i-1]**2))
        B16v.append(0.5*Q16_S[j]*(z[i]**2-z[i-1]**2))
        B22v.append(0.5*Q22_S[j]*(z[i]**2-z[i-1]**2))
        B26v.append(0.5*Q26_S[j]*(z[i]**2-z[i-1]**2))
        B66v.append(0.5*Q66_S[j]*(z[i]**2-z[i-1]**2))
        i=i+1




    B11=sum(B11v)
    B12=sum(B12v)
    B16=sum(B16v)
    B22=sum(B22v)
    B26=sum(B26v)
    B66=sum(B66v)

    # D matrix


    D11v=[]
    D12v=[]
    D16v=[]
    D22v=[]
    D26v=[]
    D66v=[]
    i=1
    for j in range(0,PlyN,1):
        D11v.append((1/3.0)*Q11_S[j]*(z[i]**3-z[i-1]**3))
        D12v.append((1/3.0)*Q12_S[j]*(z[i]**3-z[i-1]**3))
        D16v.append((1/3.0)*Q16_S[j]*(z[i]**3-z[i-1]**3))
        D22v.append((1/3.0)*Q22_S[j]*(z[i]**3-z[i-1]**3))
        D26v.append((1/3.0)*Q26_S[j]*(z[i]**3-z[i-1]**3))
        D66v.append((1/3.0)*Q66_S[j]*(z[i]**3-z[i-1]**3))
        i=i+1


    D11=sum(D11v)
    D12=sum(D12v)
    D16=sum(D16v)
    D22=sum(D22v)
    D26=sum(D26v)
    D66=sum(D66v)

    return A11,A12,A16,A22,A26,A66,B11,B12,B16,B22,B26,B66,D11,D12,D16,D22,D26,D66 










E11=125744
E22=10030
Nu12=0.271
G12=5555



Lam=[45,-45,0,90,90,0,-45,45]
PlyN=len(Lam)
LamTh=0.125


A11,A12,A16,A22,A26,A66,B11,B12,B16,B22,B26,B66,D11,D12,D16,D22,D26,D66=ABD(E11,E22,G12,Nu12,Lam,LamTh,PlyN)

print(A11,A12)


