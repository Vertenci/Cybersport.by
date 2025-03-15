document.addEventListener('DOMContentLoaded', () => {
    const loadMoreButton = document.getElementById('load-more');
    const matchesContainer = document.getElementById('matches-container');
    let offset = 10;

    if (loadMoreButton) {
        loadMoreButton.addEventListener('click', () => {
            fetch(`${window.location.href}?limit=10&offset=${offset}`, {
                headers: {
                    'x-requested-with': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {

                data.matches.forEach(match => {
                    matchesContainer.innerHTML += `
                        <a href="/matches/${match.id}/" class="match-card">
                            <div class="matches-info">
                                <div class="icon-time">
                                    <img src="${match.game_icon}" alt="game-icon" class="game-icon">
                                    <div class="date-time">${match.date}</div>
                                </div>
                                <div class="teams-score">
                                    <div class="team">
                                        <img src="${match.team_one_icon}" alt="team_one icon" class="team-icon">
                                        ${match.team_one_name}
                                    </div>
                                    <div class="vs">${match.score}</div>
                                    <div class="team">
                                        <img src="${match.team_two_icon}" alt="team_two icon" class="team-icon">
                                        ${match.team_two_name}
                                    </div>
                                </div>
                                <div class="tournament">${match.tournament}</div>
                            </div>
                        </a>
                    `;
                });

                offset += 10;

                if (!data.has_more) {
                    loadMoreButton.style.display = 'none';
                }
            })
            .catch(error => console.error('Error loading more matches:', error));
        });
    }
});
