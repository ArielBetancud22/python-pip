# Game Project

Para correr el juego se deben seguir las instrucciones
en terminal

```sh
cd game
python3 main.py
```
<br>
Por aca te presento la wiki de este proyecto en Python:</br>
https://github.com/ArielBetancud22/python-pip/wiki/Clase-1

# Entorno Virtual en Python

<br>Comenzamos con el entorno virtual en Python, para ingresar al repo después de un tiempo tuve que hacer lo siguiente, abri la terminal de Ubuntu desde window como administrador:</br>

```sh
    mkdir py-project
    cd py-project
    git clone https://...
    ll
    cd python-pip
    code .
    git branch #Solo esta la rama main
    git branch second #Comenzamos a crear nuevas ramas
    git branch profe
    git branch ariel22
    git status #Desde la rama main ya hay cambio para commitear
    git add .
    git commit -m"Agrego el archivo txt donde detallo cada parte de las clases"
    git push origin main #Surge un problema debo crear un token para poder cargar cambios
    #Se debe entrar en GitHub settings - Developer settings - Personal access tokens - token classic
    #Se genera escribiendo las notas de que trabajo se va a tratar y se deben tildar cuanto tiempo de duración tendrá el token y tildar los permisos, generar y por último copiar el token
    git pull origin main
    Usuario: ArielBetancud22
    password: accessToken #El que hemos creado y debemos guardar bien
    git config --global credential.helper store #Este comando es para guardar el token, pero habrá que ingrearlo una vez y desde allí lo recordará.
```