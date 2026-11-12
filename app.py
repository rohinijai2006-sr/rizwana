from flask  import Flask
app=Flask( __ name __ )
app.route("/")
def home():
    return "hello world "
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
