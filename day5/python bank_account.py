"""
Bank Account - Demonstrating Encapsulation and Methods
A simple banking system using OOP principles.
"""

from datetime import datetime
from typing import List, Tuple


class BankAccount:
    """
    Represents a bank account with basic operations.
    
    Attributes:
        account_number (str): Unique account identifier
        account_holder (str): Name of the account holder
        balance (float): Current account balance
        transaction_history (List[Tuple]): History of all transactions
    """
    
    # Class variable for account number generation
    _next_account_number = 1000
    
    def __init__(self, account_holder: str, initial_deposit: float = 0.0):
        """
        Initialize a new bank account.
        
        Args:
            account_holder (str): Name of the account holder
            initial_deposit (float): Initial deposit amount (default: 0.0)
        
        Raises:
            ValueError: If initial deposit is negative
        """
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative")
        
        self.account_number = f"ACC{BankAccount._next_account_number:06d}"
        BankAccount._next_account_number += 1
        
        self.account_holder = account_holder
        self._balance = initial_deposit  # Private attribute
        self.transaction_history: List[Tuple[datetime, str, float, float]] = []
        
        if initial_deposit > 0:
            self._add_transaction("Initial Deposit", initial_deposit)
    
    @property
    def balance(self) -> float:
        """
        Get the current account balance.
        
        Returns:
            float: Current balance
        """
        return self._balance
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print("❌ Deposit amount must be positive")
            return False
        
        self._balance += amount
        self._add_transaction("Deposit", amount)
        print(f"✅ Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print("❌ Withdrawal amount must be positive")
            return False
        
        if amount > self._balance:
            print(f"❌ Insufficient funds. Current balance: ${self._balance:.2f}")
            return False
        
        self._balance -= amount
        self._add_transaction("Withdrawal", -amount)
        print(f"✅ Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True
    
    def transfer(self, recipient: 'BankAccount', amount: float) -> bool:
        """
        Transfer money to another account.
        
        Args:
            recipient (BankAccount): The receiving account
            amount (float): Amount to transfer
            
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print("❌ Transfer amount must be positive")
            return False
        
        if amount > self._balance:
            print(f"❌ Insufficient funds. Current balance: ${self._balance:.2f}")
            return False
        
        self._balance -= amount
        recipient._balance += amount
        
        self._add_transaction(f"Transfer to {recipient.account_number}", -amount)
        recipient._add_transaction(f"Transfer from {self.account_number}", amount)
        
        print(f"✅ Transferred ${amount:.2f} to {recipient.account_holder}")
        return True
    
    def _add_transaction(self, description: str, amount: float) -> None:
        """
        Add a transaction to the history (private method).
        
        Args:
            description (str): Transaction description
            amount (float): Transaction amount
        """
        timestamp = datetime.now()
        self.transaction_history.append((timestamp, description, amount, self._balance))
    
    def get_statement(self, num_transactions: int = 10) -> None:
        """
        Print account statement showing recent transactions.
        
        Args:
            num_transactions (int): Number of recent transactions to show
        """
        print(f"\n{'='*70}")
        print(f"ACCOUNT STATEMENT".center(70))
        print(f"{'='*70}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self._balance:.2f}")
        print(f"{'='*70}")
        
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print(f"\n{'Date/Time':<20} {'Description':<25} {'Amount':>12} {'Balance':>12}")
            print("-" * 70)
            
            recent = self.transaction_history[-num_transactions:]
            for timestamp, desc, amount, balance in recent:
                date_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                amount_str = f"${amount:+.2f}"
                balance_str = f"${balance:.2f}"
                print(f"{date_str:<20} {desc:<25} {amount_str:>12} {balance_str:>12}")
        
        print("=" * 70)
    
    def __str__(self) -> str:
        """String representation of the account."""
        return f"BankAccount({self.account_number}, {self.account_holder}, ${self._balance:.2f})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"BankAccount(account_holder='{self.account_holder}', balance={self._balance})"


def demo():
    """Demonstrate the BankAccount class functionality."""
    print("🏦 Bank Account Demo\n")
    
    # Create accounts
    print("Creating accounts...")
    alice = BankAccount("Alice Smith", 1000.0)
    bob = BankAccount("Bob Johnson", 500.0)
    
    print(f"\n{alice}")
    print(f"{bob}\n")
    
    # Perform transactions
    print("Performing transactions...\n")
    
    alice.deposit(200)
    alice.withdraw(150)
    bob.deposit(300)
    alice.transfer(bob, 100)
    
    # Show statements
    print("\n")
    alice.get_statement()
    print("\n")
    bob.get_statement()


if __name__ == "__main__":
    demo()