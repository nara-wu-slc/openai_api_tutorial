# openai_api_tutorial
OpenAIのAPIを使ってGPT-4等のモデルを自作プログラムから利用する

#### 作業ディレクトリの作成
`/path/to/dir`は適当なディレクトリ名に読み替える（`/slc/work/ユーザ名` 以下を推奨）
```
mkdir -p /path/to/dir
```

#### Pythonの環境作り
```
cd /path/to/dir
python3 -m venv --prompt openai_api_tutorial .venv
source .venv/bin/activate
pip3 install openai
```

#### OpenAI API Keyの設定
API Keyは教員にリクエストしてもらってください
```
export OPENAI_API_KEY=Keyとして共有された文字列
```

#### サンプルプログラムの実行
```
python3 ./openai_api_test_tiny.py
```

`Success! Response dumped into c.`のようなメッセージが表示される

#### 結果の確認
ファイル名は適宜変更
```
python3 ./pickle_print.py responses/20241113_175704.884569_2bfebed8-0803-4d66-91b9-3e148f14b5b5.pkl
```

結果の例
```
ChatCompletion(id='chatcmpl-AT3TNgZlq9KSHUmc8X5eb8ryct4H2', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='My name is Nakano. I have been living near Nakano Station for fifteen years.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1731488225, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier=None, system_fingerprint='fp_0ba0d124f1', usage=CompletionUsage(completion_tokens=18, prompt_tokens=58, total_tokens=76, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
```
