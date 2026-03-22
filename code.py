from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

# Hex bytes as a string
p_hex = "00FEC3ECFB4C5D564181F77A0C66628A5D"
q_hex = "009BF26B2C78615AA375BDF190F92F5575"
e_hex = "010001"
c_hex = "87DFFC0C992C7B499BE35AFD790984FE4F7AF520FD06343DA0D3155F8179E057"

# Convert to integer
p = int(p_hex, 16)
q = int(q_hex, 16)
e = int(e_hex, 16)
c = int(c_hex, 16)

print("p =", p)
print("q =", q)
print("e =", e)
print("c =", c)

n = p * q
phi = (p-1)*(q-1)
d = inverse(e, phi)

print("d =", d)

#plaintext = b"r4D_r5a"  # your desired message as bytes
#m = bytes_to_long(plaintext)        # convert to integer
#print("m as integer:", m)

#c = pow(m, e, n)
#c_hex = hex(c)[2:].upper()
#print("c-hex: ",c_hex)

m = pow(c, d, n)

print("m = ", m)
m_trans = long_to_bytes(m)
flag = m_trans.decode('utf-8')
print(flag)
