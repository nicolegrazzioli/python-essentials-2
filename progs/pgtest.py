import pygame

run = True #vai rodar enquanto run = true
width = 400 #tamanho da janela
height = 100 #tamanho da janela
pygame.init() #inicializa ambiente pygame 
screen = pygame.display.set_mode((width, height)) #prepara a tela da aplicação 
font = pygame.font.SysFont(None, 48) #cria um objeto representando fonte tamanho 48
text = font.render("Welcome to pygame", True, (255, 255, 255)) #cria um objeto representando o texto a ser exibido (true e branco)
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2)) #insere o texto no buffer da tela (ainda invisivel)
pygame.display.flip() #atualiza a tela, tornando o texto visivel
while run: #loop principal
  for event in pygame.event.get(): #pega uma lista dos eventos pendentes
   if event.type == pygame.QUIT\
    or event.type == pygame.MOUSEBUTTONUP\
    or event.type == pygame.KEYUP: #se o evento for QUIT, clique do mouse ou tecla
    run = False #para de rodar

