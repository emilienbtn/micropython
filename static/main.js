import Tweet from "./components/Tweet";
import TweetList from "./components/TweetList";
//import cookie from 'react-cookie';

class Main extends React.Component {
    constructor(props) {
        super(props);
        //this.state = { userId: cookie.load('session') };
        this.state = { tweets: [] }
    }
    // function to post tweets
    addTweet(tweet) {
        var self = this;
        $.ajax({
            url: '/api/v1/tweets',
            contentType: 'application/json',
            type: 'POST',
            data: JSON.stringify({
                'username': "user1",
                'body': tweet,
            }),
            success: function () {
                alert("success")
                let newTweetList = self.state.tweets;
                newTweetList.unshift({ tweetedby: "user1", body: tweet, timestamp: Date.now });
                self.setState({ tweets: newTweetList })
                return;
            },
            error: function () {
                return console.log("Failed");
            }
        });
    }
    // function to pull tweets
    componentDidMount() {
        var self = this;
        $.getJSON('/api/v1/tweets', function (tweetModels) {
            var t = tweetModels
            alert(t)
            self.setState({ tweets: t })
        });
    }

    render() {
        return (
            <div>
                <Tweet sendTweet={this.addTweet.bind(this)} />
                <TweetList tweet={this.state.tweets} />
            </div>
        );
    }
}


let documentReady = () => {
    ReactDOM.render(
        <Main />,
        document.getElementById('react')
    );
};

$(documentReady);