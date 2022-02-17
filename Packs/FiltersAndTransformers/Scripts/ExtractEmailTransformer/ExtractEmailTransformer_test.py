from ExtractEmailTransformer import *
import pytest


valid_address_str = """simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com
x@example.com
example-indeed@strange-example.com
example@s.example
user%example.com@example.org
user-@example.org
test <test@test.com>"""


valid_address = [
    "simple@example.com",
    "very.common@example.com",
    "disposable.style.email.with+symbol@example.com",
    "other.email-with-hyphen@example.com",
    "fully-qualified-domain@example.com",
    "user.name+tag+sorting@example.com",
    "x@example.com",
    "example-indeed@strange-example.com",
    "example@s.example",
    "user%example.com@example.org",
    "user-@example.org",
    "test@test.com",
]


data_test_regex_create = [
    (valid_address_str, valid_address),
]


@pytest.mark.parametrize('input_str, email_address', data_test_regex_create)
def test_regex_create(input_str, email_address):
    assert list(re.findall(EMAIL_REGEX, input_str)) == email_address


data_test_main = [
    ({'value': 'test'}, []),
    ({'value': 'test@test.com'}, ['test@test.com']),
    ({'value': 'test@test.com,test?test@test.com'}, ['test@test.com', 'test@test.com']),
]


@pytest.mark.parametrize('args, command_outputs', data_test_main)
def test_main(args, command_outputs, mocker):
    mocker.patch.object(demisto, 'args', return_value=args)
    results_mocker = mocker.patch('ExtractEmailTransformer.return_results')
    main()
    results_mocker.args[0] == command_outputs
