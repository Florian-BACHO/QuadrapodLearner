##
## EPITECH PROJECT, 2018
## nanotekspice
## File description:
## Makefile
##

CXX		=	g++

SRCS		=	src/Main.cpp \
			src/AQuadripod.cpp \
			src/PhysicalQuadripod.cpp

OBJS 		= 	$(SRCS:.cpp=.o)

CXXFLAGS	= 	-Wall -Wextra -W -Werror -std=gnu++17 -g3

CPPFLAGS 	=	-I ./include

LDFLAGS		=	-lfann

NAME 		=	quadripod

all:		$(NAME)

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
