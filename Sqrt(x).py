class Solution:
    def mySqrt(self, x: int) -> int:
        mejorCandidato = (x//2)//2
        candidato = 1

        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(1, (x//2)+1):
            
            candidato = i * i
            if candidato == x:
                return i
            elif candidato > x:
                return i - 1
            
            elif x - candidato < x - mejorCandidato:
                mejorCandidato = i
        return mejorCandidato



print(Solution.mySqrt(Solution, 1))

#Esta priemra solucion es O(n) la cual funciona pero es increiblemente lenta

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            
            if sq == x:
                return mid
            elif sq < x:
                ans = mid  # Guardamos el candidato válido
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

#En cambio esta es O(log n )y es bastante sencilla de hacer 
#La clave esta en idenficiar los patrones presenes pues sabemos que si probamo sun valor podemos descartar los mayores o menores dependiendo el resultado ademas por ejemplo en este caso es un conjunto monoton ode enteros y com otenemos valores de 
#prueba muy grandes la busqueda lineal se sobre pasa

# Resumen mental para el próximo problema:
# ¿El rango de posibles respuestas está ordenado de forma lógica? (Sí)¿
# Descartar la mitad de las opciones en cada paso me garantiza no perder la respuesta correcta? (Sí)
# ¿El rango es demasiado grande para recorrerlo uno por uno? (Sí)$\rightarrow$ Aplica Búsqueda Binaria.