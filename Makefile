.PHONY: requirements start_new create_venv venv format lint run security

###############################################################################
# COMMANDS                                                                    #
###############################################################################


run: ## Executa o código main
	@python src/main.py


create_venv: ## Cria e ativa um novo ambiente virtual
	@python -m venv .venv --prompt venv
	@source ./.venv/bin/activate


venv: ## Ativa o ambiente virtual
	@source ./.venv/bin/activate


install: ## Instala as dependências do projeto com o Poetry
	@poetry install
	@maturin build --release -o packages
	@pip install packages/*.whl



format: ## Formata os arquivos .py do projeto, seguindo os padrões da PEP 8
	@isort src
	@ruff formar src


lint: ## Realiza uma análise estática
# 	@flake8 src || true
# 	@pydocstyle --add-ignore D100,D107,D104 src || true
	@ruff src || true


security: ## Realiza uma análise de segurança das bibliotecas utilizadas
	@pip-audit || true


.PHONY: help
help: ## Exibe a mensagem de ajuda
	@echo "Utilize: make <comando>"
	@echo "Comandos disponíveis:"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
