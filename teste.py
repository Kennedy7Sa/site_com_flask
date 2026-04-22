from comunidadeimpressionadora import app,database 
from comunidadeimpressionadora.models import Usuario,Post



# ************ Criando o banco 
# with app.app_context():
#     database.create_all()


#******************* Criando registros 
# with app.app_context():
#     usuario = Usuario(username = 'kennedy',email='kennedy@gmail.com',senha='123456')
#     usuario2 = Usuario(username ='mateus',email='mateus@gmail.com',senha='123456')

#     #fazendo o commit no banco 
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()

#************************ Buscando dados 
# with app.app_context():
#     #pegrando todos os usuarios 
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     #pegando dados de cada usuario 
#     meu_usuario = Usuario.query.first()
#     print(meu_usuario.id)
#     print(meu_usuario.username)
#     print(meu_usuario.email)
#     #filtrando por argumento 
#     usuario_teste = Usuario.query.filter_by(id=1).first()
#     print(usuario_teste.email)


# **************************** Criando um post
# with app.app_context():
#     post1= Post(titulo = 'Pirmeira aula',corpo='teste tetetstetst t ',id_usuario = 1)
#     database.session.add(post1)
#     database.session.commit()


#******************* pesquisando os posts relacionados aos usuarios 
# with app.app_context():
     
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.corpo)
#     print(post.data_criacao)
#     print(post.autor.username) #pegando dados da tabela usuario que esta relacionada a tabela de posts 

#### resetando o banco 
with app.app_context():
    database.drop_all() #para excluir o banco e todas as tabelas 
    database.create_all()

