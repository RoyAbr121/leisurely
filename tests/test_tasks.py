class TestAddTask:
    def test_add_returns_correct_sum(self):
        from src.tasks.example import add
        result = add.delay(3, 4)
        assert result.get() == 7

    def test_add_with_negative_numbers(self):
        from src.tasks.example import add
        result = add.delay(-5, 5)
        assert result.get() == 0

    def test_add_result_state_is_success(self):
        from src.tasks.example import add
        result = add.delay(1, 1)
        result.get()
        assert result.state == "SUCCESS"


class TestSendWelcomeEmailTask:
    def test_email_returns_sent_status(self):
        from src.tasks.example import send_welcome_email
        result = send_welcome_email.delay("user@example.com", "Alice")
        outcome = result.get()
        assert outcome["status"] == "sent"

    def test_email_returns_correct_recipient(self):
        from src.tasks.example import send_welcome_email
        result = send_welcome_email.delay("bob@example.com", "Bob")
        outcome = result.get()
        assert outcome["recipient"] == "bob@example.com"
