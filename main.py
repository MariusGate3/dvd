from dvd import Dvd
import pygame
import config
import random


def main():
    pygame.init()
    running = True
    dvd = Dvd(100, 100, (255, 0, 0))
    DVDS = [dvd]
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    corners_hit = 0
    text = font.render(f"Corners bounced off: {corners_hit}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topleft = (10, 10)
    config.screen.fill((0, 0, 0))
    config.screen.blit(text, text_rect)
    pygame.display.flip()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    can_place = True
                    for dvd in DVDS:
                        if dvd.rect.collidepoint(event.pos):
                            can_place = False
                            break
                    if can_place:
                        DVDS.append(Dvd(event.pos[0], event.pos[1], (255, 0, 0)))

        config.screen.fill((0, 0, 0))
        for dvd in DVDS:
            if (dvd.rect.left == 0 or dvd.rect.right == config.window_x) and (
                dvd.rect.top == 0 or dvd.rect.bottom == config.window_y
            ):
                corners_hit += 1

            for dvd2 in DVDS:
                if dvd != dvd2 and dvd.rect.colliderect(dvd2.rect):
                    dvd.direction = (-dvd.direction[0], -dvd.direction[1])
                    dvd.updateFont()
            dvd.update()
            dvd.draw(config.screen)

        text = font.render(f"Corners bounced off: {corners_hit}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = (config.window_x / 2 - 100, 10)
        config.screen.blit(text, text_rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
