import base64
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad ,unpad
from sign2 import send

o='ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
n='ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'

# chip='Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml664RVH6kpauKu1ZDImdC2ORD5vB_tz4bzyNPJVMqBvyRz7EjjjV2Wge34-vPJ9_RVrrXEH3p87xSX_lyEFZMIkQFg-bTU0R98-a7beygksFqkLcwuD9s-T6sXzsmTPbBSZrJGVrlMb6GJEDUSZtjtTxPZsJq413IEZ0IY9BgymM_FnepjJMNtbN5TAmiERuwcbZ7F7O_AYvSbV9JwoIEkGrVfZEspqb8qj_cDNE9wZJ3SHgcYWkqRImr6Tuhec4n1UB2S20s6ahFV7C6QiD91UHWkarHyOWWQG-oTZWa_HDTenQNaPszfocwT6OxZ2yitZFqBXu2LCvGgyfLe4obj5-heZxKCFsy2vK-yfdgDSuHfERgNc12Y5f-g-BhRkipIppoTeBO9BIKodTKhwNWA1dIUFnjWYDx2I5lRVP02Zx4='
chip=send()
chip=chip.replace("-","+").replace("_","/")

key=md5(o.encode('utf-8')).digest()
iv=md5(n.encode('utf-8')).digest()

aes=AES.new(key=key,iv=iv,mode=AES.MODE_CBC)

data=aes.decrypt(base64.b64decode(chip))
data=unpad(data,16)
print(data.decode('utf-8'))