import json
import requests

# API 키와 기본 URL 설정
TMDB_API_KEY = 'YOUR_TMDB_API_KEY'
MOVIE_INFO_URL = "https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=ko-KR"

# 기존 JSON 파일을 읽기
with open("movies.json", "r", encoding='UTF-8') as f:
    movies_data = json.load(f)

# 모든 영화 데이터를 업데이트하는 함수
def update_movies_data(movies_data):
    for movie in movies_data:
        movie_id = movie['fields']['id']  # 영화의 ID 가져오기

        # 영화 상세 정보 가져오기
        response = requests.get(MOVIE_INFO_URL.format(movie_id=movie_id, api_key=TMDB_API_KEY))
        
        if response.status_code == 200:
            movie_details = response.json()

            # runtime 및 production_country 추가
            runtime = movie_details.get('runtime', None)  # 상영시간 정보
            production_countries = movie_details.get('production_countries', [])
            production_country = production_countries[0]['name'] if production_countries else None

            # 기존 JSON 데이터에 runtime 및 production_country 추가
            movie['fields']['runtime'] = runtime
            movie['fields']['production_country'] = production_country

            print(f"Updated movie: {movie['fields']['title']}, runtime: {runtime}, production_country: {production_country}")
        else:
            print(f"Failed to get details for movie ID {movie_id}, Status code: {response.status_code}")

    return movies_data

# 영화 데이터를 업데이트하고 저장
updated_movies_data = update_movies_data(movies_data)

# 업데이트된 JSON 데이터를 다시 저장
with open("updated_movies.json", "w", encoding='UTF-8') as f:
    json.dump(updated_movies_data, f, indent=4, ensure_ascii=False)
