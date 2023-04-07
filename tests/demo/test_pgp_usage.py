import textwrap

import pgpy
from loguru import logger
from pgpy.constants import HashAlgorithm

from python_boilerplate.common.profiling import cpu_profile, elapsed_time, mem_profile
from python_boilerplate.demo.pgp_usage import (
    alice_public_key,
    alice_secret_key,
    bob_public_key,
    bob_secret_key,
)


@elapsed_time("INFO")
@mem_profile("INFO")
@cpu_profile("INFO")
def test_when_alice_sends_message_to_bob():
    plaintext = "Hello World!"
    signature = pgpy.PGPMessage.new(plaintext)
    assert signature is not None
    # sign a message
    # the bitwise OR operator "|" is used to add a signature to a PGPMessage.
    signature |= alice_secret_key.sign(signature, hash=HashAlgorithm.SHA512)
    assert signature is not None
    logger.info(f'The signature for "{plaintext}" is:\n{str(signature)}')
    encrypted = bob_public_key.encrypt(signature)
    assert encrypted is not None
    logger.info(f"The signed encrypted is:\n{str(encrypted)}")

    decrypted = bob_secret_key.decrypt(encrypted)
    assert decrypted is not None
    assert decrypted.message is not None
    assert plaintext == decrypted.message
    logger.info(f"The decrypted: {decrypted.message}")
    verified = alice_public_key.verify(decrypted)
    assert verified is not None


@elapsed_time("INFO")
@mem_profile("INFO")
@cpu_profile("INFO")
def test_when_bob_sends_message_to_alice():
    plaintext = "Hello World!"
    signature = pgpy.PGPMessage.new(plaintext)
    assert signature is not None
    # sign a message
    # the bitwise OR operator "|" is used to add a signature to a PGPMessage.
    signature |= bob_secret_key.sign(signature, hash=HashAlgorithm.SHA512)
    assert signature is not None
    logger.info(f'The signature for "{plaintext}" is:\n{str(signature)}')
    encrypted = alice_public_key.encrypt(signature)
    assert encrypted is not None
    logger.info(f"The signed encrypted is:\n{str(encrypted)}")

    decrypted = alice_secret_key.decrypt(encrypted)
    assert decrypted is not None
    assert decrypted.message is not None
    assert plaintext == decrypted.message
    logger.info(f"The decrypted: {decrypted.message}")
    verified = bob_public_key.verify(decrypted)
    assert verified is not None


@elapsed_time("INFO")
@mem_profile("INFO")
@cpu_profile("INFO")
def test_load_armor_ciphertext_and_then_verify():
    message_text = textwrap.dedent(
        """\
        -----BEGIN PGP MESSAGE-----

        wcDMA+ncLmW9GlBZAQv8DE6tT4ncRzg/+49v4lM93eksvHvJgl7vQ9FBnWN+VMrt
        gySvhVUTh80lkrH1yWTxgpcclzO9TLb1yyxCIBm2tLkw4PUfZ863NlI/iYSQvo6f
        3XFcYqhcjRtUqIb+6/twuAsL40Nj6pRXnHLCHdAvi1VotC8LsVC0aG5BozN+FDZV
        TSLbaWuXrmY5dlR17Vguncaazp0G6MXg6dvyIP/OyBFn6r9W02/+BTfPR00pRQFt
        oS58yPF+/NmeuC6mEBuR5hN93yWPo9DJgpf3bQrKbpecU6pmjalkXV7qsDZuNGVV
        opEvis+PlU2jJVmwPT8eUIFNbz2d1HIOoF5GGBqvWchWaV19FbxcnF3qk/hBzzFh
        mJLTcAKozcr/RPwY8ppdyOVmfjzdu802BAHrmtKYDj1Xz0+9nOP9tsKVHKaQ1wY4
        d2zLjMj6a3q7sOBzABtarR5aKdKhibvrEGz27iWyVgJjQ5tTtB29gVZaBjn5yvfO
        E6SgHc2XI+y+dWt6dFk30sFLAVEf7F88Sr0yZsBwMDcPgK7OGMkwcpU2iDkUp3Ww
        7PTILmyAu0yL/mzTzPNBLUOwiWLz1TWfjReopZzlWi2SyKHAkYo0YcTGJoUDLFmy
        gRaXs2VTEyGY4c1Ivxuy2+QRN9uVi3LKflL0Ay3/h8LXydVH7IO7xsCu+TDYiX5A
        C+v8mP6ATzw/9bze4cnv9BR6guylpr1DyVHHNAkkvtGhNW0ASj5xFiWtOiVwxOm6
        06jrD2BiE7KZdHIWgI07H0UnY7i0miVHVKmLgpr74Ctq5LqCTn14a42ObsJblghg
        Wa+ymdMLNLsKsTu3G1XLiHF/xJjlVyFjykggqL0hAR1k3rRtShou/9iH90T2VTvr
        HTV7EmXH6fn/NnTlMG4o1oTZf9vImGvUywdIsuxojV0bw1Kitf36x+Y+XY299JiW
        6VqE5/MxPEE5GesBgjZeKJAZp+6x6GxnIijEaycDqYRMw80rEgzJyOhP9+JdJ6JS
        v5YTAxagpLdnpwqJw6KQLjIHrZLSJNBxRJ5GcQ0hxUmlpxMz01eoNSePq2Nos5hf
        4i2OabOo6Hy92BQG/czhIaXLt7rRbH05cYfYc6q+QXtTNIOEkJIQRfkUnMMvJKLq
        QnqIc+AQ+Cx12LHKewpxAXm1gQfnKxUm5BwvgCmP1HklJgJa5MqpFjNeoPxiJkqc
        ICtXJXKuK/MGXL2q8Q==
        =I73S
        -----END PGP MESSAGE-----
        """
    )
    message = pgpy.PGPMessage.from_blob(message_text)
    assert message is not None
    decrypted = alice_secret_key.decrypt(message)
    assert decrypted is not None
    assert decrypted.message == "Hello World!"
    verified = bob_public_key.verify(decrypted)
    assert verified is not None
    logger.info(f"{verified}")
