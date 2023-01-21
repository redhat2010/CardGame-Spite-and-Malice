from card import *
from deck import Deck
from image_creator import *
from card_stack import *
import pygame
import time

# create the decks
player1_deck = Deck()
player2_deck = Deck()
center_deck = Deck()

# empty hands
player1_hand = []
player2_hand = []

# generate the deck & distribute initial cards
center_deck.gen_deck(num_decks=2)
center_deck.shuffle()
player1_deck.insert_cards(center_deck.draw(23))
player2_deck.insert_cards(center_deck.draw(23))
center_deck.shuffle()
player1_deck.shuffle()
player2_deck.shuffle()
player1_hand = center_deck.draw(5)
player2_hand = center_deck.draw(5)

# create and initialize the stacks
center_stacks = [CenterStack(), CenterStack(),CenterStack(), CenterStack()]
player1_stacks = [SideStack(),SideStack(),SideStack(),SideStack()]
player2_stacks = [SideStack(),SideStack(),SideStack(),SideStack()]

# create card compare object
card_comp = CardCompare()

# create card drawer
card_creator = CardImageCreator()

# Initilize the display
gameDisplay = pygame.display.set_mode((1000, 1000))

# Load the board image and display it
board_img = pygame.image.load("images/spite_and_malice/board.png")
#gameDisplay.blit(board_img,(0,0))
gameDisplay.blit(board_img, (0,0))
pygame.display.update()
card_back = pygame.image.load("images/card_back.png")
card_spot = pygame.image.load("images/card_spot.png")

black = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 24)
p1_card_count = font.render("", True, black)
p2_card_count = font.render("", True, black)


#run the game
game_state = 1
turn = 1
allow_switch = True
while game_state != 0:
    gameDisplay.blit(board_img, (0,0))
    
    # display the player's hands
    # if allow_switch is on, switches which hand is visible, otherwise only player 1's hand is visible
    for i in range(len(player1_hand)):
        if turn != 1 and allow_switch:
            gameDisplay.blit(pygame.transform.scale(card_back,(125,175)), (175 + i*125,900))
        else:
            gameDisplay.blit(pygame.transform.scale(card_creator.create_card(player1_hand[i]),(125,175)), (175 + i*125,900))
    for i in range(len(player2_hand)):
        if turn == 2 and allow_switch:
            gameDisplay.blit(pygame.transform.scale(card_creator.create_card(player2_hand[i]),(125,175)), (175 + i*125,-64))
        else:
            gameDisplay.blit(pygame.transform.scale(card_back,(125,175)), (175 + i*125,-64))

    # displays the center stacks
    for i in range(len(center_stacks)):
        cur_card = center_stacks[i].check_top()
        if cur_card != None:
            gameDisplay.blit(pygame.transform.scale(card_creator.create_card(cur_card),(125,175)), (275 + i*150,413))
        else:
            gameDisplay.blit(pygame.transform.scale(card_spot,(125,175)),(275 + i*150,413))
    

    # displays player 1's side stacks
    for i in range(len(player1_stacks)):
        cur_card = player1_stacks[i].check_top()
        if cur_card != None:
            gameDisplay.blit(pygame.transform.scale(card_creator.create_card(cur_card),(125,175)), (275 + i*150,650))
        else:
            gameDisplay.blit(pygame.transform.scale(card_spot,(125,175)),(275 + i*150,650))

    # displays player 2's side stacks
    for i in range(len(player2_stacks)):
        cur_card = player2_stacks[i].check_top()
        if cur_card != None:
            gameDisplay.blit(pygame.transform.scale(card_creator.create_card(cur_card),(125,175)), (275 + i*150,175))
        else:
            gameDisplay.blit(pygame.transform.scale(card_spot,(125,175)),(275 + i*150,175))

    # displays the draw pile
    if center_deck.cards_left() > 0:
        gameDisplay.blit(pygame.transform.scale(card_back,(125,175)),(50,413))
    else:
        gameDisplay.blit(pygame.transform.scale(card_spot,(125,175)),(50,413))

    # displays player 1's deck
    cur_card = player1_deck.check(1)
    if cur_card != None:
        gameDisplay.blit(pygame.transform.scale(card_creator.create_card(cur_card),(125,175)),(50,650))
    else:
        gameDisplay.blit(pygame.transform.scale(card_spot,(125,175)),(50,650))
    p1_card_count = font.render("Cards Left: " + str(player1_deck.cards_left()), True, black)
    gameDisplay.blit(p1_card_count,(50,625))

    # displays player 2's deck
    cur_card = player2_deck.check(1)
    if cur_card != None:
        gameDisplay.blit(pygame.transform.scale(card_creator.create_card(cur_card),(125,175)),(50,175))
    else:
        gameDisplay.blit(pygame.transform.scale(card_spot,(125,175)),(50,175))
    p2_card_count = font.render("Cards Left: " + str(player2_deck.cards_left()), True, black)
    gameDisplay.blit(p2_card_count,(50,150))

    pygame.display.update()

    # handle the events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                game_state = 0
            if event.key == pygame.K_LSHIFT:
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
        elif event.type == pygame.QUIT:
            pygame.quit()
            x = 1
        else:
            pass