import json

import pytest


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["pawn", "d4", "d5"],
        ["pawn", "a2", "a4"],
        ["pawn", "a6", "a7"],
        ["pawn", "h7", "h8"],
    ],
)
def test_pawn_valid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "pawn"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "null"


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["pawn", "d4", "a5"],
        ["pawn", "d4", "d6"],
        ["pawn", "h1", "h2"],
        ["pawn", "a8", "a9"],
    ],
)
def test_pawn_invalid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "pawn"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Current move is not permitted."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["pawn", "d400", "e5"],
        ["pawn", "d-10", "c5"],
        ["pawn", "h9", "g5"],
        ["pawn", "h10", "a8"],
    ],
)
def test_pawn_invalid_field_validation_move(
    test_app,
    chess_figure,
    curr_field,
    dest_field,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 409
    assert data["figure"] == "pawn"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Field does not exist."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["pawny", "d4", "d5"],
        ["pawnggy", "d3", "d4"],
        ["pawn_", "a2", "a4"],
        ["pawntt", "h2", "h3"],
    ],
)
def test_pawn_invalid_name_validation_move(
    test_app,
    chess_figure,
    curr_field,
    dest_field,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert data["figure"] == chess_figure
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == f"Chess figure - {chess_figure} - does not exist."


@pytest.mark.parametrize(
    "chess_figure, curr_field, available_moves",
    [
        ["pawn", "h2", ["h3", "h4"]],
        ["pawn", "a1", []],
        ["pawn", "b5", ["b6"]],
    ],
)
def test_pawn_available_moves(test_app, chess_figure, curr_field, available_moves):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == chess_figure
    assert data["currentField"] == curr_field
    assert data["availableMoves"].sort() == available_moves.sort()
    assert data["error"] == "null"


@pytest.mark.parametrize(
    "chess_figure, curr_field, available_moves",
    [
        ["pawn", "d40b0", []],
        ["pawn", "a1o0", []],
        ["pawn", "h-04", []],
        ["pawn", "h9", []],
    ],
)
def test_pawn_invalid_field_available_moves(
    test_app,
    chess_figure,
    curr_field,
    available_moves,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 409
    assert data["figure"] == chess_figure
    assert data["currentField"] == curr_field
    assert data["availableMoves"] == []
    assert data["error"] == "Field does not exist."


@pytest.mark.parametrize(
    "chess_figure, curr_field, available_moves",
    [
        ["pawny", "d4", []],
        ["p_wn", "d4", []],
        ["pawn_ie", "h4", []],
        ["pawnie", "h1", []],
    ],
)
def test_pawn_invalid_name_available_moves(
    test_app,
    chess_figure,
    curr_field,
    available_moves,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert data["figure"] == chess_figure
    assert data["currentField"] == curr_field
    assert data["availableMoves"] == []
    assert data["error"] == f"Chess figure - {chess_figure} - does not exist."
