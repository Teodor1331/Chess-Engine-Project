# pylint: disable=E1101

"""Tests on the module with the methods for building the chess board."""

from unittest import mock

import pygame

from game_graphics import IMAGES
from game_graphics import PIECES
from game_graphics import ELEMENTS
from game_graphics import load_pieces


def test_images_constant():
    """Test the module constant IMAGES."""
    assert isinstance(IMAGES, dict)
    assert len(IMAGES.keys()) == 0
    assert len(IMAGES.values()) == 0


def test_pieces_constant():
    """Test the module constant PIECES."""
    assert isinstance(PIECES, dict)
    assert len(PIECES.keys()) == 6
    assert len(PIECES.values()) == 6

    assert PIECES['P'] == 'Pawn'
    assert PIECES['R'] == 'Rook'
    assert PIECES['N'] == 'Knight'
    assert PIECES['B'] == 'Bishop'
    assert PIECES['Q'] == 'Queen'
    assert PIECES['K'] == 'King'


def test_elements_constant():
    """Test the module constant ELEMENTS."""
    assert isinstance(ELEMENTS, list)
    assert isinstance(ELEMENTS[0], list)
    assert isinstance(ELEMENTS[1], list)

    assert ELEMENTS[0][0] == '../images/White Pieces/White_'
    assert ELEMENTS[1][0] == '../images/Black Pieces/Black_'
    assert ELEMENTS[0][1] == 'PRNBQK'
    assert ELEMENTS[1][1] == 'prnbqk'


def test_loading_and_drawing_methods():
    """Test the loading and drawing methods."""
    with mock.patch('game_graphics.ELEMENTS') as mocked_elements:
        mocked_elements = [
            [('../' + ELEMENTS[0][0]), ELEMENTS[0][1]],
            [('../' + ELEMENTS[1][0]), ELEMENTS[1][1]],
        ]

        assert 'mocked_elements' in locals()
        assert locals()['mocked_elements'] is mocked_elements

        screen = pygame.display.set_mode((512, 512), flags=pygame.HIDDEN)
        screen.fill(pygame.Color('white'))

        assert isinstance(load_pieces(), type(None))
