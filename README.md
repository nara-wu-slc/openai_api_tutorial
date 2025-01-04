# openai_api_tutorial
OpenAIのAPIを使ってGPT-4等のモデルを自作プログラムから利用する

## 目次
- [共通の事前作業](#共通の事前作業)
- [基本形：自分でプログラムを書く場合の参考](#基本形自分でプログラムを書く場合の参考)
- [応用形1：プロンプトをコマンドラインオプションやファイルで与える](#応用形1プロンプトをコマンドラインオプションやファイルで与える)

## 共通の事前作業
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
API Keyは教員にリクエストして取得してください
```
export OPENAI_API_KEY=Keyとして共有された文字列
```

## 基本形：自分でプログラムを書く場合の参考
#### サンプルプログラムの実行
```
python3 ./openai_api_test_tiny.py
```

`Success! Response dumped into responses/20241113_175704.884569_2bfebed8-0803-4d66-91b9-3e148f14b5b5.pkl.`のようなメッセージが表示される

#### 結果の確認
ファイル名は適宜変更
```
python3 ./pickle_print.py responses/20241113_175704.884569_2bfebed8-0803-4d66-91b9-3e148f14b5b5.pkl
```

結果の例
```
ChatCompletion(id='chatcmpl-AT3TNgZlq9KSHUmc8X5eb8ryct4H2', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='My name is Nakano. I have been living near Nakano Station for fifteen years.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1731488225, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier=None, system_fingerprint='fp_0ba0d124f1', usage=CompletionUsage(completion_tokens=18, prompt_tokens=58, total_tokens=76, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
```

## 応用形1：プロンプトをコマンドラインオプションやファイルで与える
#### コマンドの内容詳細
```
python3 run_chat_completion.py -h
```
でヘルプメッセージが表示される。
- `-v` または `--verbose`: デバッグメッセージを表示
- `-m` または `--model`: OpenAIのモデルを指定（標準は `gpt-4o-mini`）
- `-s` または `--system`: システムプロンプトが記載されたファイル名を指定
- `-S` または `--system-prompt`: システムプロンプトの文字列を指定
- `-u` または `--user`: ユーザプロンプトが記載されたファイル名を指定
- `-U` または `--user-prompt`: ユーザプロンプトの文字列を指定
- `-o` または `--output`: 出力される `.pkl` ファイルの名前（標準は日時＋ランダム文字列）
- `-d` または `--dir`: 出力される `.pkl` ファイルが可能されるディレクトリの名前（標準は `responses`）

#### 実行コマンド
サンプルコマンドを走らせてみる
```
python3 run_chat_completion.py -o sample
```
正常終了すると
```
Success! Response dumped into responses/sample.pkl.
```
と表示され、`responses/sample.pkl`というファイルが作成される。

#### 出力コマンド
pickle形式で保存された応答結果からテキスト部分を取り出す
```
python3 print_chat_completion.py responses/sample.pkl
```

実行すると以下のように表示される

```
Certainly! Here are some useful tips for using the OpenAI API effectively:

1. **Understand the Endpoint**: Familiarize yourself with the different endpoints (e.g., completions, chat, and embeddings) and choose the one that best suits your needs.

2. **Use Proper Models**: Select the appropriate model for your task. For example, for general conversation, you might choose the GPT models; for embeddings, you would use the embedding models.

3. **Craft Effective Prompts**: The quality of your prompts significantly impacts the output. Be clear and specific about what you want. For example:
   - Instead of asking, "Tell me about dogs," you could ask, "What are the key characteristics of Golden Retrievers as family pets?"

4. **Adjust the Temperature**: Use the temperature parameter to control randomness. A lower value (e.g., 0.2) will make the output more deterministic, while a higher value (e.g., 0.8) will provide more varied responses.

5. **Set Max Tokens**: Use the `max_tokens` parameter to limit the length of the generated response. This helps control costs and ensures that the responses are concise.

6. **Utilize Stop Sequences**: Use stop sequences to dictate where the model should end output. This can be particularly useful to prevent overly long or rambling responses.

7. **Temperature and Top-p Together**: Experiment with both `temperature` and `top_p` parameters for more nuanced control over the creativity and focus of the outputs.

8. **Fine-tuning (when available)**: If your use case requires, consider using fine-tuning features (where applicable) to customize the model on your specific data, particularly in business-specific scenarios.

9. **Use System Messages**: In chat-based models, utilize system messages to set up context or guidelines for the conversation, influencing the behavior of the assistant.

10. **Batch Requests**: If you need multiple completions, use batch requests to save on latency and make better use of your API calls.

11. **Error Handling**: Implement error handling in your code to manage situations where the API might fail or return unexpected results. This can help maintain smooth user experiences.

12. **Stay Updated**: Follow OpenAI's updates and documentation as features and best practices can evolve. Check for new models or changes that might benefit your implementation.

13. **Monitor Usage**: Keep an eye on your API usage and costs. Use the monitoring tools provided by OpenAI to understand your consumption patterns better.

14. **Experiment and Iterate**: Don’t hesitate to experiment with different parameters, inputs, and approaches to see what works best for your application or use case.

15. **Community and Support**: Utilize community forums, documentation, and OpenAI’s support for troubleshooting and sharing best practices with other developers.

By following these tips, you can enhance your experience with the OpenAI API and leverage its capabilities effectively for your projects.
```

## 応用形2：プロンプトに
