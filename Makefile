##
## EPITECH PROJECT, 2018
## nanotekspice
## File description:
## Makefile
##

CXX		=	g++

SRCS		=	src/Main.cpp

OBJS 		= 	$(SRCS:.cpp=.o)

CXXFLAGS	= 	-Wall -Wextra -W -Werror -std=gnu++17

CPPFLAGS 	=	-I ./include -I ./include/components

NAME 		=	quadripod

all:		$(NAME)

debug:		$(CXXFLAGS) += -g3

debug: 		re

run: 		re
		./$(NAME)

$(NAME):	$(OBJS)
		$(CXX) -o $(NAME) $(OBJS) $(LDFLAGS)

clean:
		$(RM) $(OBJS)

fclean: 	clean
		$(RM) $(NAME)

re:		fclean all

.PHONY:		all clean fclean re debug run
