# #!/usr/bin/python3
# """Message model for Ikiru web app"""
# import models
# from sqlalchemy import Column, ForeignKey, String
# from sqlalchemy.orm import relationship
# from models.base_model import Base, BaseModel


# class Message(BaseModel, Base):
#     """Message Class"""
#     __tablename__ = 'messages'
#     text = Column(String(2048), nullable=False)
    
#     # Foreign keys
#     conversation_id = Column(String(36),
#                              ForeignKey("conversations.id"), nullable=False)
#     user_id = Column(String(36), ForeignKey("users.id"), nullable=False)

#     # relationships
#     conversations = relationship("Conversation", back_populates="messages")
    
    
