
from .db import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = (
        db.UniqueConstraint("email", name="uq_users_email"),
        db.Index("ix_users_is_active", "is_active"),
        db.Index("ix_users_registered_at", "registered_at"),
    )

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable = False)
    midddleName = db.Column(db.String(50), nullable = True)
    lastName = db.Column(db.String(50), nullable = True)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=True)  # optional if using OAuth
    is_active = db.Column(db.Boolean, nullable=False, server_default=db.text("1"))
    is_verified = db.Column(db.Boolean, nullable=False, server_default=db.text("0"))
    role = db.Column(db.String(32), nullable=False, server_default=db.text("'user'"))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    last_login_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

#   # relationships (kept light; aligns with Reservation.user_id ON DELETE SET NULL)
#     reservations = db.relationship(
#         "Reservation",
#         back_populates="user",
#         passive_deletes=True,   # let DB handle SET NULL (no orphan delete)
#     )  

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return bool(self.password_hash) and check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email!r} active={self.is_active}>"

    

    # # relationships
    # reservations = db.relationship(
    #     "Reservation",
    #     back_populates="user",
    #     cascade="all, delete-orphan",
    #     passive_deletes=True,
    # )

    # def __repr__(self):
    #     return f"<User {self.id} {self.full_name!r}>"


# class ParkingLot(db.Model):
#     __tablename__ = "parking_lots"

#     id = db.Column(db.Integer, primary_key=True)
#     prime_location_name = db.Column(db.String(150), nullable=False)
#     price = db.Column(db.Numeric(10, 2), nullable=True)           # e.g., per hour
#     address = db.Column(db.Text, nullable=True)
#     pin_code = db.Column(db.String(20), index=True, nullable=True)
#     number_of_spots = db.Column(db.Integer, nullable=True)

#     created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
#     updated_at = db.Column(
#         db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False
#     )

#     # relationships
#     spots = db.relationship(
#         "ParkingSpot",
#         back_populates="lot",
#         cascade="all, delete-orphan",
#         passive_deletes=True,
#     )

#     def __repr__(self):
#         return f"<ParkingLot {self.id} {self.prime_location_name!r}>"


# class ParkingSpot(db.Model):
#     __tablename__ = "parking_spots"

#     id = db.Column(db.Integer, primary_key=True)
#     lot_id = db.Column(
#         db.Integer,
#         db.ForeignKey("parking_lots.id", ondelete="CASCADE"),
#         nullable=False,
#         index=True,
#     )
#     status = db.Column(
#         db.Enum("O", "A", name="spot_status"),  # O=occupied, A=available
#         nullable=False,
#         default="A",
#         index=True,
#     )

#     created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
#     updated_at = db.Column(
#         db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False
#     )

#     # relationships
#     lot = db.relationship("ParkingLot", back_populates="spots")
#     reservations = db.relationship(
#         "Reservation",
#         back_populates="spot",
#         cascade="all, delete-orphan",
#         passive_deletes=True,
#     )

#     def __repr__(self):
#         return f"<ParkingSpot {self.id} lot={self.lot_id} status={self.status}>"


# class Reservation(db.Model):
#     __tablename__ = "reservations"

#     id = db.Column(db.Integer, primary_key=True)
#     spot_id = db.Column(
#         db.Integer,
#         db.ForeignKey("parking_spots.id", ondelete="CASCADE"),
#         nullable=False,
#         index=True,
#     )
#     user_id = db.Column(
#         db.Integer,
#         db.ForeignKey("users.id", ondelete="SET NULL"),
#         nullable=True,
#         index=True,
#     )

#     parking_timestamp = db.Column(
#         db.DateTime, server_default=db.func.now(), nullable=False, index=True
#     )
#     leaving_timestamp = db.Column(db.DateTime, nullable=True, index=True)
#     parking_cost = db.Column(db.Numeric(10, 2), nullable=True)

#     created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
#     updated_at = db.Column(
#         db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False
#     )

#     # relationships
#     spot = db.relationship("ParkingSpot", back_populates="reservations")
#     user = db.relationship("User", back_populates="reservations")

#     def __repr__(self):
#         return f"<Reservation {self.id} spot={self.spot_id} user={self.user_id}>"
