from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    # Store user information
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)


class SetPiece(Base):
    # Links sets and pieces needed with quantities and colors
    __tablename__ = "set_pieces"
    set_id = Column(Integer, ForeignKey("sets.set_id"), primary_key=True)
    piece_id = Column(Integer, ForeignKey("pieces.piece_id"), primary_key=True)
    color_code = Column(Integer, ForeignKey("colors.color_code"), primary_key=True)
    quantity = Column(Integer)


class Set(Base):
    # Stores information about different sets
    __tablename__ = "sets"
    set_id = Column(Integer, primary_key=True,)
    set_name = Column(String, index=True)
    pieces = relationship("SetPiece", backref="set")


class Color(Base):
    # Stores color information
    __tablename__ = "colors"
    color_code = Column(Integer, primary_key=True)
    color_name = Column(String, index=True)


class Piece(Base):
    # Stores information about individual pieces.
    __tablename__ = "pieces"
    piece_id = Column(Integer, primary_key=True)
    part_number = Column(Integer)
    color_code = Column(Integer, ForeignKey("colors.color_code"))
    sets = relationship("SetPiece", backref="piece")


class Inventory(Base):
    # Stores the inventory of pieces for each user.
    __tablename__ = "inventory"
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    piece_id = Column(Integer, ForeignKey("pieces.piece_id"), primary_key=True)
    color_name = Column(String, ForeignKey("colors.color_name"), primary_key=True)
    piece_part_number = Column(Integer, ForeignKey("pieces.part_number"))
    quantity = Column(Integer)
