# Pechincha+ — plataforma de ofertas em Django

Projeto demonstrativo de uma plataforma de ofertas, inspirado em padrões de navegação de sites de promoções, mas com marca, textos e interface próprios.

## Recursos
- Página inicial com destaques e ofertas recentes
- Busca por produto, categoria ou loja
- Filtros por recentes, preço, desconto e popularidade
- Categorias e lojas
- Detalhe de oferta com preço antigo, preço atual, desconto e cupom
- Favoritos para usuários logados
- Votação das ofertas
- Alertas de preço
- Carrinho demonstrativo
- Finalização demonstrativa (sem cobrança real)
- Cadastro/login
- Área Minha Conta
- Newsletter
- Formulário de contato
- Cupons
- Django Admin completo
- Dados de demonstração via `seed_demo`

## Rodar no VS Code / Windows
1. Extraia a pasta.
2. Abra a pasta no VS Code.
3. Terminal > New Terminal.
4. Rode `./run.bat` ou `run.bat`.
5. Acesse http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/
Usuário: `admin`
Senha: `admin12345`

Troque a senha antes de publicar.

## Observação
As URLs de lojas, imagens e produtos do `seed_demo` são apenas dados de demonstração. Para produção, substitua por dados reais, políticas de privacidade, domínio, e-mail, armazenamento de imagens e gateway de pagamento, se necessário.
