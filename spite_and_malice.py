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

# create and initialize the stacks
center_stacks = [CenterStack(), CenterStack(),CenterStack(), CenterStack()]
player1_stacks = [SideStack(),SideStack(),SideStack(),SideStack()]
player2_stacks = [SideStack(),SideStack(),SideStack(),SideStack()]