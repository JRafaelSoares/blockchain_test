import unittest
from blockchain.blockchain_data_structure import Transaction
from crypto.keygen import generate_key_pair

class TestTransactionClass(unittest.TestCase):

    # Should we use constants to better represent tests or global variables for correct cases ?
    node_identifier = "test"
    from_address = "from_address"
    to_address = "to_address"
    amount = 1
    generate_key_pair(node_identifier)

    # ------------------------------------- #
    # --------- Constructor Tests --------- #
    # ------------------------------------- #

    def test_constructor_correct(self):
        transaction = Transaction("from_address", "to_address", 1)
        self.assertEqual(transaction.fromAddress, "from_address")
        self.assertEqual(transaction.toAddress, "to_address")
        self.assertEqual(transaction.amount, 1)

    def test_constructor_null_to_address(self):
        with self.assertRaises(Exception):
            Transaction("from_address", None, 1)

    def test_constructor_negative_amount(self):
        with self.assertRaises(Exception):
            Transaction("from_address", "to_address", -1)

    def test_constructor_none_amount(self):
        with self.assertRaises(Exception):
            Transaction("from_address", "to_address", None)

    # TODO - Add to and from address type check test
    # TODO - Add amount type check test

    # --------------------------------------- #
    # ----------- Integrity Tests ----------- #
    # --------------------------------------- #

    # TODO - How to test if hashing is correct in itself

    def test_integrity_modified_id(self):
        transaction = self.get_correct_transaction()
        self.assertFalse(transaction.check_valid("fake_id"))

    def test_integrity_modified_from_address(self):
        transaction = self.get_correct_transaction()
        transaction.fromAddress = "fake_from_address"
        self.assertFalse(transaction.check_valid(self.node_identifier))

    def test_integrity_modified_to_address(self):
        transaction = self.get_correct_transaction()
        transaction.toAddress = "fake_to_address"
        self.assertFalse(transaction.check_valid(self.node_identifier))

    def test_integrity_modified_amount(self):
        transaction = self.get_correct_transaction()
        transaction.amount = 2
        self.assertFalse(transaction.check_valid(self.node_identifier))

    def test_integrity_modified_signature(self):
        transaction = self.get_correct_transaction()
        transaction.signature = bytes('test', encoding='utf-8')
        self.assertFalse(transaction.check_valid(self.node_identifier))

    # ------------------------------------ #
    # ----------- Aux Function ----------- #
    # ------------------------------------ #

    # Returns a correctly made and signed transaction
    def get_correct_transaction(self):
        transaction = Transaction("from_address", "to_address", 1)
        transaction.sign_transaction(self.node_identifier)
        return transaction


if __name__ == '__main__':
    unittest.main()