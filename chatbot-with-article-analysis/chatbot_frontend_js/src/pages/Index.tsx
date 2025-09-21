import { useState, useRef, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Send, Loader2 } from "lucide-react";
interface ChatMessage {
  question: string;
  response: string;
  timestamp: Date;
}
interface ChatRequest {
  user_question: string;
  user_email: string;
  session_id: string;
  article_url: string;
}
interface ChatResponse {
  status: string;
  webhook_status: number;
  session_id: string;
  data: {
    output: string;
  };
}
const Index = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [formData, setFormData] = useState({
    user_question: "",
    user_email: "",
    session_id: "",
    article_url: ""
  });
  
  // Ref for auto-scroll functionality
  const messagesEndRef = useRef<HTMLDivElement>(null);
  
  // Auto-scroll to bottom when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.user_question.trim()) return;
    setIsLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: {
          'accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData as ChatRequest)
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data: ChatResponse = await response.json();
      setMessages(prev => [...prev, {
        question: formData.user_question,
        response: data.data.output,
        timestamp: new Date()
      }]);
      setFormData(prev => ({
        ...prev,
        user_question: ""
      }));
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prev => [...prev, {
        question: formData.user_question,
        response: "Error: Could not connect to the server. Please check if the API is running.",
        timestamp: new Date()
      }]);
    } finally {
      setIsLoading(false);
    }
  };
  return <div className="min-h-screen bg-background p-4">
      <div className="mx-auto max-w-4xl">
        <Card className="mb-6">
          <CardHeader>
            <CardTitle>Chat Informations</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <Label htmlFor="email">User Email</Label>
                <Input id="email" type="email" value={formData.user_email} onChange={e => setFormData(prev => ({
                ...prev,
                user_email: e.target.value
              }))} placeholder="your@email.com" />
              </div>
              <div>
                <Label htmlFor="session">Session ID</Label>
                <Input id="session" value={formData.session_id} onChange={e => setFormData(prev => ({
                ...prev,
                session_id: e.target.value
              }))} placeholder="session123" />
              </div>
            </div>
            <div>
              <Label htmlFor="article">Article URL</Label>
              <Input id="article" type="url" value={formData.article_url} onChange={e => setFormData(prev => ({
              ...prev,
              article_url: e.target.value
            }))} placeholder="https://example.com/article" />
            </div>
          </CardContent>
        </Card>

        <Card className="h-96 mb-4">
          <CardHeader>
            <CardTitle>Chat Messages</CardTitle>
          </CardHeader>
          <CardContent className="p-0">
            <ScrollArea className="h-80 p-4">
              {messages.length === 0 ? <p className="text-muted-foreground text-center py-8">No messages yet. Start a conversation!</p> : <div className="space-y-4">
                  {messages.map((message, index) => <div key={index} className="space-y-2">
                      <div className="bg-primary text-primary-foreground p-3 rounded-lg ml-auto max-w-[80%]">
                        <p className="text-sm">{message.question}</p>
                      </div>
                      <div className="bg-muted p-3 rounded-lg mr-auto max-w-[80%]">
                        <p className="text-sm whitespace-pre-wrap">{message.response}</p>
                        <p className="text-xs text-muted-foreground mt-1">
                          {message.timestamp.toLocaleTimeString()}
                        </p>
                      </div>
                    </div>)}
                  {/* Auto-scroll anchor */}
                  <div ref={messagesEndRef} />
                </div>}
            </ScrollArea>
          </CardContent>
        </Card>

        <form onSubmit={handleSubmit} className="flex gap-2">
          <Textarea value={formData.user_question} onChange={e => setFormData(prev => ({
          ...prev,
          user_question: e.target.value
        }))} placeholder="Type your question..." className="min-h-[60px] flex-1" onKeyDown={e => {
          if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
          }
        }} />
          <Button type="submit" disabled={isLoading || !formData.user_question.trim()} className="self-end">
            {isLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : <Send className="h-4 w-4" />}
          </Button>
        </form>
      </div>
    </div>;
};
export default Index;