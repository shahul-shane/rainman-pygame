import pygame, random , time
pygame.font.init()

width, height = 800, 600

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space')

bg = pygame.transform.scale(pygame.image.load('bg.jpg'), (width, height))

font = pygame.font.SysFont('conicsans', 30)
def draw(player, elapsed_time, stars):
    win.blit(bg, (0, 0))
    
    time_text = font.render(f"Time : {round(elapsed_time)}s", 1, 'white')
    win.blit(time_text, (10, 10))
    pygame.draw.rect(win, 'red', player)
    for star in stars:
        pygame.draw.rect(win, 'white', star)
    pygame.display.update()

player_width = 40
player_height = 60
player_vel = 5

star_width = 10
star_height = 20
star_vel = 3

def main():
    run = True

    player = pygame.Rect(200, height - player_height, player_width, player_height)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit= False 
    while run:
        star_count += clock.tick(60)

        elapsed_time = time.time() - start_time
        draw(player, elapsed_time, stars)

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, width - star_width)
                star = pygame.Rect(star_x,  star_height, star_width, star_height)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            run = False
            break

        if keys[pygame.K_LEFT] and player.x - player_vel >=0:
            player.x -= player_vel

        if keys[pygame.K_RIGHT] and player.x + player_vel + player.width <= width:
            player.x += player_vel

        for star in stars[:]:
            star.y += star_vel
            if star.y > height:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            lost_text = font.render('you lost', 1 , 'white')
            win.blit(lost_text, (width /2 - lost_text.get_width(), height/2 - lost_text.get_width()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

    pygame.quit()


if __name__ == '__main__':
    main()