# Python 3 programı - Özyinelemeli (recursive) ikili arama (binary search).
# Eski Python 2 için yapılması gereken değişiklikler yorum satırlarında belirtilmiştir.

# Eğer x dizide varsa, x'in indeksini döndürüyorum, yoksa -1 döndürüyorum
def binary_search(arr, low, high, x):

    # Temel durumu kontrol ediyorum
    if high >= low:

        # Ortadaki elemanın indeksini buluyorum
        mid = (high + low) // 2

        # Eğer eleman ortadaki eleman ise
        if arr[mid] == x:
            # Ortadaki elemanın indeksini döndürüyorum
            return mid

        # Eğer eleman ortadaki elemandan küçükse
        # sol alt dizide arama yapıyorum
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Eğer eleman ortadaki elemandan büyükse
        # sağ alt dizide arama yapıyorum
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Eleman dizide yoksa -1 döndürüyorum
        return -1

# Test dizisi oluşturuyorum
arr = [2, 3, 4, 10, 40]
# Aranacak elemanı belirliyorum
x = 10

# Fonksiyonu çağırıyorum
result = binary_search(arr, 0, len(arr)-1, x)

# Sonucu kontrol ediyorum ve yazdırıyorum
if result != -1:
    print("Eleman dizide mevcut, indeksi:", str(result))
else:
    print("Eleman dizide mevcut değil")
