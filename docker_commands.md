# Docker Commands Cheat Sheet

Commands used so far in the ai-switch-log project, with what each one does.

## Key words

| Word | Meaning |
|---|---|
| Image | A packaged template (app plus everything it needs). Read-only. |
| Container | A running (or stopped) copy of an image. |
| Dockerfile | A text recipe that says how to build an image. |
| Tag | A name or version label on an image, like `hello-py` or `python:3.12-slim`. |
| Port mapping | A link between a port on your Mac and a port inside a container. |
| Volume | Storage kept outside a container so data survives if the container is deleted. |

## 1. Checking Docker

| Command | What it does |
|---|---|
| `docker --version` | Shows the installed Docker version. |
| `docker ps` | Lists **running** containers. |
| `docker ps -a` | Lists all containers, including stopped ones. |
| `docker images` | Lists images stored on your Mac. |

## 2. Running containers

| Command | What it does |
|---|---|
| `docker run <image>` | Creates a container from an image and starts it. Downloads the image first if it is missing. |
| `docker run --rm <image>` | Same, but deletes the container when it finishes. Good for short scripts. |
| `docker run -d <image>` | Runs in the background ("detached"). Use for long-running things like a database. |
| `--name <name>` | Gives the container a name, so you can refer to it later. |
| `-p 1521:1521` | Maps port `HOST:CONTAINER`. Traffic to port 1521 on your Mac goes to port 1521 in the container. |
| `-e NAME=value` | Passes an environment variable into the container (for example a password). |

The Oracle database container was started with:

```
docker run -d --name oracle-free -p 1521:1521 -e ORACLE_PASSWORD='...' gvenzl/oracle-free:slim
```

## 3. Managing containers

| Command | What it does |
|---|---|
| `docker stop <name>` | Stops a running container. Data inside is kept. |
| `docker start <name>` | Starts a stopped container again. |
| `docker logs <name>` | Shows what the container has printed. |
| `docker logs -f <name>` | Follows the logs live. Press Ctrl + C to stop watching. |
| `docker logs --tail 20 <name>` | Shows only the last 20 lines. |
| `docker exec -it <name> bash` | Opens a shell inside a running container. |
| `docker exec <name> <command>` | Runs one command inside a running container. |
| `docker rm <name>` | Deletes a stopped container and any data inside it. |
| `docker rm -f <name>` | Force-deletes a container, even a running one. |

## 4. Building your own image

Example `Dockerfile`:

```
FROM python:3.12-slim
WORKDIR /app
COPY hello.py .
CMD ["python", "hello.py"]
```

| Line | What it does |
|---|---|
| `FROM` | The base image to start from (here, one with Python 3.12 already installed). |
| `WORKDIR` | The working folder inside the image. Created if it does not exist. |
| `COPY` | Copies files from your Mac into the image. |
| `RUN` | Runs a command while building, such as `pip install ...`. |
| `CMD` | The command that runs when a container starts. |

| Command | What it does |
|---|---|
| `docker build -t hello-py .` | Builds an image named `hello-py` from the Dockerfile in the current folder. |
| `docker run --rm hello-py` | Runs a container from that image. |
| `docker run --rm hello-py cat /app/hello.py` | Runs a one-off command inside the image to check its contents. |
| `docker rmi <image>` | Deletes an image. |

Remember: an image holds a **copy** of your files from build time. After changing a file, rebuild the image.

## 5. Common problems

| Problem | Likely cause and fix |
|---|---|
| `docker: command not found` | Docker Desktop is not running yet, or the Terminal window is old. Start Docker and open a new Terminal. |
| `Cannot connect to the Docker daemon` | Docker Desktop is not running. Open it and wait for "Engine running". |
| Container does not show in `docker ps` | It has exited. Use `docker ps -a`. |
| `docker run` prints nothing | The script has no output, or the file was not saved before the build. |
| `ORA-` or connection fails right after start | The database is still starting. Wait for `DATABASE IS READY TO USE!` in `docker logs`. |
| Data disappeared | The container was deleted without a volume. |

## 6. Safe habits

1. Do not click the trash icon on a container you want to keep.
2. Use `docker ps -a` and `docker images` to see what is on your machine.
3. Never put passwords in a Dockerfile or in an image.
4. Use `--rm` for throwaway runs so stopped containers do not pile up.
5. Stop containers and quit Docker Desktop when you are done, to save battery and memory.
