docker run -t --user $(id -u):$(id -g) -v "$(pwd)":/workspace latex_container /bin/bash -c "cd /workspace; $@"