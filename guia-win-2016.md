# Instlación de OpenSSH en Windows Server 2016

  - Descargar OpenSSH(64)
  - Descomprimirlo en C:\
  - Configurar sshd_config
  - Descomentar las líneas
```
RSAAuthentication yes
PUVKeyAuthentication yes
```
  - Ejecutamos el instalador vía PowerShell en Administrador
  `.\install-sshd.ps1`
  - Ejecutamos la configuración
  `Set-Service sshd -StartupType Automatic; Set-Service ssh-agent -StartupType Automatic; Start-Service sshd; Start-Service ssh-agent`

# Configuración de OpenSSH

 - Ejecutar PowerShell
 ```bash
 # Set the sshd service to be started automatically
Get-Service -Name sshd | Set-Service -StartupType Automatic

# Now start the sshd service
.\Start-Service sshd
```

## Generación de llaves

Ejecutamos el generador de llaves:
`.\ssh-keygen -t ecdsa`
Todas las preguntas por defecto vacías.

Las llaves creadas se encuentran en el directorio indicado por la salida prompt.
`C:\Users\Administrador\.ssh`

# Configuración de arranque

```bash
# By default the ssh-agent service is disabled. Configure it to start automatically.
# Make sure you're running as an Administrator.
Get-Service ssh-agent | Set-Service -StartupType Automatic

# Start the service
Start-Service ssh-agent

# This should return a status of Running
Get-Service ssh-agent

# Now load your key files into ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ecdsa
```

### Crear una llave ed25519
`ssh-keygen -t ed25519`


----------------------------

# Instlación en Widnows Server 2016

  - Instalar el archivo: ` OpenSSH-Win64-v9.8.1.0.msi`
  - Descargado del repositorio: `https://github.com/PowerShell/Win32-OpenSSH/releases`
  - Ejecutar como administrador el Explorador de Archivos de windows y ejecutar el instalador.
  - El instalador se instalará en el directorio `C:\Programs Files\OpenSSH`

# Configuración
