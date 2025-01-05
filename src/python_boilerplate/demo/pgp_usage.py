from typing import Final

from loguru import logger
from pgpy import PGPKey

from python_boilerplate.common.common_function import get_resources_dir

_alice_public_key_path = get_resources_dir() / "pgp-keys/Johnny Miller's PGP Example - Alice_0x3A9AA381_public.asc"
alice_public_key: Final[PGPKey] = PGPKey.from_file(_alice_public_key_path.__str__())[0]
_alice_secret_key_path = get_resources_dir() / "pgp-keys/Johnny Miller's PGP Example - Alice_0x3A9AA381_SECRET.asc"
alice_secret_key: Final[PGPKey] = PGPKey.from_file(_alice_secret_key_path.__str__())[0]

_bob_public_key_path = get_resources_dir() / "pgp-keys/Johnny Miller's PGP Example - Bob_0xAF34CAD3_public.asc"
bob_public_key: Final[PGPKey] = PGPKey.from_file(_bob_public_key_path.__str__())[0]
_bob_secret_key_path = get_resources_dir() / "pgp-keys/Johnny Miller's PGP Example - Bob_0xAF34CAD3_SECRET.asc"
bob_secret_key: Final[PGPKey] = PGPKey.from_file(_bob_secret_key_path.__str__())[0]

logger.warning(
    f"""
    Done reading PGP keys.
    Alice PGP public key: {alice_public_key.fingerprint}
                 created: {alice_public_key.created}
    Alice PGP SECRET key: {alice_secret_key.fingerprint}
                 created: {alice_secret_key.created}
    Bob's PGP public key: {bob_public_key.fingerprint}
                 created: {bob_public_key.created}
    Bob's PGP SECRET key: {bob_secret_key.fingerprint}
                 created: {bob_secret_key.created}
    """.lstrip()
)
